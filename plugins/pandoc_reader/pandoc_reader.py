import subprocess
from pelican import signals
from pelican.readers import BaseReader
from pelican.utils import pelican_open
import frontmatter
import re


class PandocReader(BaseReader):
    enabled = True
    file_extensions = ['md', 'markdown', 'mkd', 'mdown']

    def read(self, filename):
        with pelican_open(filename) as fp:
            metadata, content = frontmatter.parse(fp)

        ###################
        #  set up pandoc  #
        ###################
        extra_args = self.settings.get('PANDOC_ARGS', [])
        extensions = self.settings.get('PANDOC_EXTENSIONS', [])

        # bibliography processing
        bibliography = metadata.get("bibliography", False) or\
              self.settings.get('PANDOC_BIB', '')
        csl = metadata.get("csl", False) or\
              self.settings.get('PANDOC_CSL', '')
        bibprocess = ''
        if bibliography and csl:
            bibprocess = ['--filter',
                          'pandoc-citeproc',
                          '--bibliography',
                          './bib/' + bibliography,
                          '--csl',
                          './bib/' + csl]

        if isinstance(extensions, list):
            extensions = ''.join(extensions)

        pandoc_cmd = ["pandoc", "--from=markdown" + extensions, "--to=html5"]
        pandoc_cmd.extend(extra_args)
        pandoc_cmd.extend(bibprocess)


        ################
        #  run pandoc  #
        ################
        proc = subprocess.Popen(pandoc_cmd,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE)

        output = proc.communicate(content.encode('utf-8'))[0].decode('utf-8')
        status = proc.wait()
        if status:
            raise subprocess.CalledProcessError(status, pandoc_cmd)

        # TG: fix for broken {filename} past pandoc 1.15
        output = output.replace('%7Bfilename%7D', '{filename}')
        output = output.replace('%7Bstatic%7D', '{static}')


        #####################
        #  extract summary  #
        #####################
        start_sep = self.settings.get('PANDOC_SUMMARY_SEPARATOR_START',
                                      '<!-- START_SUMMARY_BLOCK -->')
        end_sep = self.settings.get('PANDOC_SUMMARY_SEPARATOR_END',
                                    '<!-- END_SUMMARY_BLOCK -->')
        
        # only extract summary if user hasn't supplied it
        if 'summary' not in metadata: 
            # text = output.splitlines()
            summary = ''
            segments = re.split(r"(" +
                                re.escape(start_sep) +
                                r"|" +
                                re.escape(end_sep) +
                                r")",
                                output,
                                re.DOTALL)
            try:
                start = segments.index(start_sep)
                end = segments.index(end_sep)
                if start < end:
                    summary = segments[start+1]
                    output = ''.join(segments[:start] +
                                     segments[start+1:end] +
                                     segments[end+1:])
            except ValueError:
                # we'll just rely on the Pelican default
                pass
            if summary:
                # make sure we start with <p>
                summary = re.sub(r"^\s*(<p>)?", "<p>", summary, re.DOTALL)
                # and end with </p>
                if not re.match(r".*</p>.*",
                                summary.split("<p>")[-1],
                                re.DOTALL):
                    summary += "</p>"
                metadata['summary'] = summary


        #########################
        #  metadata processing  #
        #########################
        # date is parsed as datetime object, convert back to string
        if metadata.get("date"):
            metadata["date"] = metadata["date"].strftime("%Y-%m-%d")
        
        # tags and authors must be comma-separated lists for pelican
        for x in ("tags", "authors"):
            if isinstance(metadata.get(x), list):
                metadata[x] = ", ".join(metadata[x])

        # remove bibliography key
        try:
            del metadata['bibliography']
        except KeyError:
            pass

        # final processing of metadata via Pelican
        for key, val in metadata.items():
            metadata[key] = self.process_metadata(key, val)


        return output, metadata


def add_reader(readers):
    for ext in PandocReader.file_extensions:
        readers.reader_classes[ext] = PandocReader


def register():
    signals.readers_init.connect(add_reader)
