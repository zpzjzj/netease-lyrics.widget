command: "export LANG=zh_CN.UTF-8; /usr/local/opt/coreutils/libexec/gnubin/timeout 1 /usr/local/bin/python3 lyrics.widget/lyrics.py"

refreshFrequency: 300 # ms

render: (output) ->
  data = if output then JSON.parse(output) else {}
  name = data["title"] or name or ""
  """
    <h1>#{name}</h1>
    <h1>#{data["a"] or ""}</h1>
    <h1>#{data["b"] or ""}</h1>
  """

style: """
  color: #006104 
  text-align: center
  right: 5%
"""