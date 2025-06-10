+++
type = "question"
title = "What is causing this error when I try to update OSM data"
description = '''I&#x27;m still trying to get openstreetmap-tiles-update-expire to run correctly. I have managed to figure out that I needed the python3 versions of the psycopg2, shapely and lxml for the current trim_osc.py, but now I&#x27;ve run into this error. My initial Google search didn&#x27;t provide anything helpful, and I...'''
date = "2018-05-31T06:46:00Z"
lastmod = "2018-05-31T19:33:00Z"
weight = 63902
keywords = [ "openstreetmap", "update" ]
aliases = [ "/questions/63902" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What is causing this error when I try to update OSM data](/questions/63902/what-is-causing-this-error-when-i-try-to-update-osm-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63902-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm still trying to get openstreetmap-tiles-update-expire to run correctly. I have managed to figure out that I needed the python3 versions of the psycopg2, shapely and lxml for the current trim_osc.py, but now I've run into this error. My initial Google search didn't provide anything helpful, and I'm just not sure where to start with this.</p>
<p>I'm running Ubuntu 18.04 server with all updates applied, and I completed the steps shown in <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">switch2osm for 18.04</a>. I am using the <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1604_tileserver_load#Updating_your_database_as_people_edit_OpenStreetMap">steps outlined here</a>, as modified above to account of Python3.</p>
<p>I should also add that I had java-related errors running Osmosis. The basic error showed as "the trustAnchors parameter must be non-empty." Researched, and was able to apply the <a href="https://stackoverflow.com/a/50103533/3079062">solution described here</a>.</p>
<p>Any help understanding what is going on is appreciated.</p>
<p>-Tim</p>
<pre><code>[2018-05-31 05:25:21] 32203 filtering diff
Traceback (most recent call last):
  File &quot;/home/&lt;user&gt;/src/regional/trim_osc.py&quot;, line 103, in &lt;module&gt;
    tree = etree.parse(options.osc if not options.gzip else gzip.GzipFile(fileobj=options.osc))
  File &quot;src/lxml/etree.pyx&quot;, line 3426, in lxml.etree.parse
  File &quot;src/lxml/parser.pxi&quot;, line 1860, in lxml.etree._parseDocument
  File &quot;src/lxml/parser.pxi&quot;, line 1880, in lxml.etree._parseFilelikeDocument
  File &quot;src/lxml/parser.pxi&quot;, line 1775, in lxml.etree._parseDocFromFilelike
  File &quot;src/lxml/parser.pxi&quot;, line 1186, in lxml.etree._BaseParser._parseDocFromFilelike
  File &quot;src/lxml/parser.pxi&quot;, line 600, in lxml.etree._ParserContext._handleParseResultDoc
  File &quot;src/lxml/parser.pxi&quot;, line 706, in lxml.etree._handleParseResult
  File &quot;src/lxml/etree.pyx&quot;, line 316, in lxml.etree._ExceptionContext._raise_if_stored
  File &quot;src/lxml/parser.pxi&quot;, line 370, in lxml.etree._FileReaderContext.copyToBuffer
  File &quot;/usr/lib/python3.6/gzip.py&quot;, line 276, in read
    return self._buffer.read(size)
  File &quot;/usr/lib/python3.6/_compression.py&quot;, line 68, in readinto
    data = self.read(len(byte_view))
  File &quot;/usr/lib/python3.6/gzip.py&quot;, line 463, in read
    if not self._read_gzip_header():
  File &quot;/usr/lib/python3.6/gzip.py&quot;, line 406, in _read_gzip_header
    magic = self._fp.read(2)
  File &quot;/usr/lib/python3.6/gzip.py&quot;, line 91, in read
    self.file.read(size-self._length+read)
  File &quot;/usr/lib/python3.6/codecs.py&quot;, line 321, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: &#39;utf-8&#39; codec can&#39;t decode byte 0x8b in position 1: invalid start byte
[2018-05-31 05:25:22] 32203 [error] Trim_osc error</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 May '18, 06:46</strong></p>
<img src="https://secure.gravatar.com/avatar/9d2fa479c7f7984fd8fd435b2badbc4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tim_rohrer&#39;s gravatar image" />
<p><span>tim_rohrer</span><br />
<span class="score" title="81 reputation points">81</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tim_rohrer has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 May '18, 16:18</strong> </span></p>
</div>
</div>
<div id="comments-container-63902" class="comments-container">
<span id="63905"></span>
<div id="comment-63905" class="comment">
<div id="post-63905-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just for completeness - what versions of things do you have installed? I'm guessing Ubuntu 18.04 + the stuff you get by installing <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a> plus the stuff from <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#Updating_your_database_as_people_edit_OpenStreetMap">https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#Updating_your_database_as_people_edit_OpenStreetMap</a> ? If so that <em>should</em> all work together (though I haven't installed a server from scratch like that in a month or so).</p>
</div>
<div id="comment-63905-info" class="comment-info">
<span class="comment-age">(31 May '18, 09:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63915"></span>
<div id="comment-63915" class="comment">
<div id="post-63915-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. You're absolutely right that I should have included that.</p>
</div>
<div id="comment-63915-info" class="comment-info">
<span class="comment-age">(31 May '18, 16:19)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
</div>
<div id="comment-tools-63902" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63902-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63904"></span>

<div id="answer-container-63904" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63904-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tim_rohrer has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is about 75% guesswork so I could be way off, but:</p>
<p>It looks like something is trying to read gzip data from a file which was not opened in binary mode. It also looks like the file was opened by the argparse module, controlled by this line:</p>
<pre><code>parser.add_argument(&#39;osc&#39;, type=argparse.FileType(&#39;r&#39;), help=&#39;input osc file, &quot;-&quot; for stdin&#39;)</code></pre>
<p>Try changing 'r' to 'rb' and see whether that makes any difference. This should probably be done conditionally on the '-z' flag, but I have no idea how to do that with argparse...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 May '18, 08:25</strong></p>
<img src="https://secure.gravatar.com/avatar/80abc4597de5aeb507c5a7ccd4ccee7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="turepalsson&#39;s gravatar image" />
<p><span>turepalsson</span><br />
<span class="score" title="836 reputation points">836</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="turepalsson has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-63904" class="comments-container">
<span id="63916"></span>
<div id="comment-63916" class="comment">
<div id="post-63916-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That bought me about 15 lines :-)</p>
<p>[2018-05-31 15:26:19] 23082 start import from seq-nr 2990717, replag is 2 day(s) and 19 hour(s) [2018-05-31 15:26:19] 23082 downloading diff [2018-05-31 15:26:47] 23082 filtering diff Traceback (most recent call last): File "/home/tileserver/src/regional/trim_osc.py", line 118, in &lt;module&gt; nodesM.append(long(node.get('id'))) NameError: name 'long' is not defined [2018-05-31 15:26:48] 23082 [error] Trim_osc error [2018-05-31 15:26:48] 23082 resetting state</p>
<p>Pastebin of the output: <a href="https://pastebin.com/nyiGgwyV">https://pastebin.com/nyiGgwyV</a></p>
<p>openstreetmap-tiles-update-expire complains "rm: cannot remove '/var/lib/mod_tile/dirty_tiles.23082': No such file or directory"</p>
<p>When should dirty_tiles be created?</p>
</div>
<div id="comment-63916-info" class="comment-info">
<span class="comment-age">(31 May '18, 16:35)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
<span id="63920"></span>
<div id="comment-63920" class="comment">
<div id="post-63920-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The long() thing looks like something is trying to run python2 code with a python3 interpreter.</p>
</div>
<div id="comment-63920-info" class="comment-info">
<span class="comment-age">(31 May '18, 17:15)</span> <span class="comment-user userinfo">turepalsson</span>
</div>
</div>
<span id="63922"></span>
<div id="comment-63922" class="comment">
<div id="post-63922-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is running now. Not sure how long the import diff should take? The original data file was from the 28th, and I'm only covering the US state of California?</p>
</div>
<div id="comment-63922-info" class="comment-info">
<span class="comment-age">(31 May '18, 18:18)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
<span id="63923"></span>
<div id="comment-63923" class="comment">
<div id="post-63923-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's a bit "how long is a piece of string" :)</p>
<p>On hardware that imports the British Isles in 4 or so hours it normally takes another 3 to catch up from 30 hours behind. You might be able to work something out from that...</p>
</div>
<div id="comment-63923-info" class="comment-info">
<span class="comment-age">(31 May '18, 18:38)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63924"></span>
<div id="comment-63924" class="comment">
<div id="post-63924-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That does help, I think. My import of California only took a few minutes; unfortunately, I failed to capture an exact time, but it wasn't long.</p>
<p>This has been running for close to an hour now. Four <code>postgres</code> processes running up high in <code>top</code>. So, I'll let it continue. It seems to be taking a lot longer than the original import.</p>
</div>
<div id="comment-63924-info" class="comment-info">
<span class="comment-age">(31 May '18, 18:47)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
<span id="63926"></span>
<div id="comment-63926" class="comment not_top_scorer">
<div id="post-63926-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Cool. It looks like the entire thing ran for about an hour and a half. I finally got "Done with import" in the log.</p>
<p>Weirdly, my other terminal session froze; second time that has happened. But, that is an different problem :-)</p>
<p>Thanks!</p>
<p>p.s. I opened an issue with <a href="https://github.com/Zverik/regional/issues">https://github.com/Zverik/regional/issues</a> regarding the binary read and the <code>long</code>. I'd like to hear some validation of these issues, and then I'd be willing to write up something for the wiki.</p>
</div>
<div id="comment-63926-info" class="comment-info">
<span class="comment-age">(31 May '18, 19:33)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
</div>
<div id="comment-tools-63904" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-63904-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

