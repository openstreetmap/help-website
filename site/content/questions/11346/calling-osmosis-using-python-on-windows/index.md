+++
type = "question"
title = "Calling osmosis using Python on Windows"
description = '''How do I structure a command to call osmosis using Python on Win 7? I want to use Python so that I can loop through several different bounding boxes For example, if I use the following command I can call osmosis: import subprocess subprocess.call([&#x27;J:/osmosis-0.40.1/bin/osmosis.bat&#x27;])  If try passin...'''
date = "2012-03-19T19:59:00Z"
lastmod = "2014-11-25T13:23:00Z"
weight = 11346
keywords = [ "python", "osmosis" ]
aliases = [ "/questions/11346" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Calling osmosis using Python on Windows](/questions/11346/calling-osmosis-using-python-on-windows)

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
<span id="post-11346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11346-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I structure a command to call <code>osmosis</code> using Python on Win 7? I want to use Python so that I can loop through several different bounding boxes</p>
<p>For example, if I use the following command I can call osmosis:</p>
<pre><code>import subprocess
subprocess.call([&#39;J:/osmosis-0.40.1/bin/osmosis.bat&#39;])</code></pre>
<p>If try passing more arguments using this approach I get an error:</p>
<pre><code>import subprocess    
subprocess.call([&#39;J:/osmosis-0.40.1/bin/osmosis.bat&#39;, &#39;--read-xml&#39;, &#39;enableDateParsing=no&#39;, &#39;file=&quot;J:/DATA/OSM/massachusetts.osm.bz2&quot;&#39;, &#39;--bounding-box top=42.48 left=-71.31 bottom=42.23 right=42.48&#39;, &#39;--write-xml&#39;, &#39;file=&quot;J:/DATA/OSM/extracted_using_py.osm.bz2&quot;&#39;])</code></pre>
<p>This question is based on my earlier <a href="http://help.openstreetmap.org/questions/11330/using-osmosis-bzcat-and-postgresql">question</a> today about using osmosis/bzcat. I'm not sure how to break up my arguments (and I've tried a lot of different options).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Mar '12, 19:59</strong></p>
<img src="https://secure.gravatar.com/avatar/2045d6b31de30983e8e020345da6cf55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="djq&#39;s gravatar image" />
<p><span>djq</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="djq has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11346" class="comments-container">
<span id="38786"></span>
<div id="comment-38786" class="comment">
<div id="post-38786-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What error do you get?</p>
</div>
<div id="comment-38786-info" class="comment-info">
<span class="comment-age">(25 Nov '14, 13:23)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
</div>
<div id="comment-tools-11346" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11346-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

