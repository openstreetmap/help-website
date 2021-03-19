+++
type = "question"
title = "pyShark crashes due to no proper UTF8 encoding"
description = '''Hey folks, I need to sniff in Pyhton using pyShark on Windows. On UNIX systems I didn&#x27;t have any problems. On Windows a strange error occurs: &amp;gt;&amp;gt;&amp;gt; cap = pyshark.LiveCapture(interface=nwdev) &amp;gt;&amp;gt;&amp;gt; cap.sniff(timeout=10) Traceback (most recent call last):  File &quot;&amp;lt;stdin&amp;gt;&quot;, line 1, i...'''
date = "2016-04-06T22:31:00Z"
lastmod = "2016-04-14T23:52:00Z"
weight = 51447
keywords = [ "python", "pyshark" ]
aliases = [ "/questions/51447" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [pyShark crashes due to no proper UTF8 encoding](/questions/51447/pyshark-crashes-due-to-no-proper-utf8-encoding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51447-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hey folks,</p><p>I need to sniff in Pyhton using pyShark on Windows. On UNIX systems I didn't have any problems.</p><p>On Windows a strange error occurs:</p><pre><code>&gt;&gt;&gt; cap = pyshark.LiveCapture(interface=nwdev)
&gt;&gt;&gt; cap.sniff(timeout=10)
Traceback (most recent call last):
  File &quot;&lt;stdin&gt;&quot;, line 1, in &lt;module&gt;
  File &quot;C:\Users\mu\WinPython-32bit-2.7.10.3\python-2.7.10
\lib\site-packages\pyshark\capture\capture.py&quot;, line 109, in load_packets
    self.apply_on_packets(keep_packet, timeout=timeout)
  File &quot;C:\Users\mu\WinPython-32bit-2.7.10.3\python-2.7.10
\lib\site-packages\pyshark\capture\capture.py&quot;, line 201, in apply_on_packets
    return self.eventloop.run_until_complete(coro)
  File &quot;C:\Users\mu\WinPython-32bit-2.7.10.3\python-2.7.10
\lib\site-packages\trollius\base_events.py&quot;, line 300, in  un_until_complete
    return future.result()
  File &quot;C:\Users\mu\WinPython-32bit-2.7.10.3\python-2.7.10
\lib\site-packages\trollius\futures.py&quot;, line 287, in result 
    raise self._exception
lxml.etree.XMLSyntaxError: Input is not proper UTF-8, indicate encoding !
Bytes: 0xE4 0x69 0x73 0x63, line 6, column 69
&gt;&gt;&gt;</code></pre><p>I work on a 32 bit Python version.</p><p>I even tried - I know that's very dangerous -</p><pre><code>reload(sys)
sys.setdefaultencoding(&#39;utf8&#39;)</code></pre><p>right in front of my pyshark call and in the parent processes. Without success.</p><p>Hope somebody is more familiar with pyShark running on Win. Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">python pyshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '16, 22:31</strong></p><img src="https://secure.gravatar.com/avatar/4526b4a9678e26be254a524e449eaa5c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elektm&#39;s gravatar image" /><p>elektm<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elektm has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Apr '16, 23:26</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-51447" class="comments-container"></div><div id="comment-tools-51447" class="comment-tools"></div><div class="clear"></div><div id="comment-51447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51695"></span>

<div id="answer-container-51695" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51695-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>After putting a lot of effort into the problem and spending a lot of time on searching for the error on the wrong place, I finally managed it to work.</p><p>It seems to be the problem, that the incoming data (in XML format) is not encoded the right way and pyshark does not cast to 'UTF-8'. While debugging it posed that it appeared to be in 'latin-1'.</p><p>I did the following:</p><ul><li>I checked out the source from Github (<a href="https://github.com/KimiNewt/pyshark.git)">https://github.com/KimiNewt/pyshark.git)</a></li><li><p>added following line between line 26 + 27 in src\pyshark\tshark\tshark_xml.py:</p><p><code>xml_pkt = xml_pkt.decode('latin-1')</code></p></li><li><p><code>python setup.py install</code> and done</p></li></ul><p>Took a lot of work and energy, but finaly solved for me!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '16, 23:52</strong></p><img src="https://secure.gravatar.com/avatar/4526b4a9678e26be254a524e449eaa5c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elektm&#39;s gravatar image" /><p>elektm<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elektm has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Apr '16, 23:55</p></div></div><div id="comments-container-51695" class="comments-container"></div><div id="comment-tools-51695" class="comment-tools"></div><div class="clear"></div><div id="comment-51695-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

