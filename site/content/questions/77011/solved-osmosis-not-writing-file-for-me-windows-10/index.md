+++
type = "question"
title = "[Solved] osmosis not writing file for me - Windows 10"
description = '''I apologise for such a silly question as I realise I must be doing something really silly. All help will be greatly appreciated. The command  osmosis --read-xml &quot;C:&#92;Users&#92;John&#92;Desktop&#92;Test.osm&quot; --write-xml &quot;C:&#92;Users&#92;John&#92;Desktop&#92;fred.osm&quot;  does not write fred.osm. osmosis runs and I get: C:&#92;Users&#92;Jo...'''
date = "2020-10-08T18:14:00Z"
lastmod = "2020-10-08T19:27:00Z"
weight = 77011
keywords = [ "windows", "10", "osmosis" ]
aliases = [ "/questions/77011" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[Solved\] osmosis not writing file for me - Windows 10](/questions/77011/solved-osmosis-not-writing-file-for-me-windows-10)

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
<span id="post-77011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77011-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I apologise for such a silly question as I realise I must be doing something really silly. All help will be greatly appreciated.</p>
<p>The command</p>
<pre><code>osmosis --read-xml &quot;C:\Users\John\Desktop\Test.osm&quot; --write-xml &quot;C:\Users\John\Desktop\fred.osm&quot;</code></pre>
<p>does not write fred.osm. osmosis runs and I get:</p>
<p><em>C:\Users\John\Desktop&gt;osmosis --read-xml "C:\Users\John\Desktop\Test.osm" --write-xml "C:\Users\John\Desktop\fred.osm" C:\Users\John\Desktop&gt;"C:\Program Files (x86)\Osmosis\bin\osmosis.bat"Oct 08, 2020 4:58:36 PM &gt; org.openstreetmap.osmosis.core.Osmosis run INFO: Osmosis Version 0.48.3 Oct 08, 2020 4:58:36 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Preparing pipeline. Oct 08, 2020 4:58:36 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Launching pipeline execution. Oct 08, 2020 4:58:36 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Pipeline executing, waiting for completion. Oct 08, 2020 4:58:36 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Pipeline complete. Oct 08, 2020 4:58:36 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Total execution time: 786 milliseconds.</em></p>
<p>Setup.</p>
<ol>
<li>I copied osmosis to C:\Program Files (x86)\osmosis.</li>
<li>Test.osm is on the desktop.</li>
<li>I have Java 8 Update 261 and Java Update 261 (64 bit) installed</li>
<li>I started a CMD window and entered <code>osmosis --read-xml "C:\Users\John\Desktop\Test.osm" --write-xml "C:\Users\John\Desktop\fred.osm"</code></li>
<li>I tried without paths as <code>osmosis --read-xml Test.osm --write-xml fred.osm</code> but it did not write</li>
<li><p>Test.osm contains</p>
<p>&lt;?xml version="1.0" encoding="UTF-8"?&gt; &lt;osm version="0.6" generator="ANW"&gt; &lt;bounds minlat="49.7667486" minlon="-8.1628456" maxlat="60.8081270" maxlon="1.7604432"/&gt; &lt;node id="1152921504610000001" lat="57.1496060" lon="-2.0969160" user="nobody" uid="1" visible="true" version="1" changeset="1" timestamp="2013-01-25T01:21:31Z"&gt; &lt;tag k="amenity" v="postal_code"/&gt; &lt;tag k="name" v="AB10 1AB"/&gt; &lt;/node&gt; &lt;node id="1152921504610000002" lat="57.1487070" lon="-2.0978060" user="nobody" uid="1" visible="true" version="1" changeset="1" timestamp="2013-01-25T01:21:31Z"&gt; &lt;tag k="amenity" v="postal_code"/&gt; &lt;tag k="name" v="AB10 1AF"/&gt; &lt;/node&gt; &lt;/osm&gt;</p></li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-10" rel="tag" title="see questions tagged &#39;10&#39;">10</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Oct '20, 18:14</strong></p>
<img src="https://secure.gravatar.com/avatar/a99494537d2727b5ac2d5e58ddd6793b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John-Ha&#39;s gravatar image" />
<p><span>John-Ha</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John-Ha has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Oct '20, 20:39</strong> </span></p>
</div>
</div>
<div id="comments-container-77011" class="comments-container">
&#10;</div>
<div id="comment-tools-77011" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77011-form-container" class="comment-form-container">
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

<span id="77013"></span>

<div id="answer-container-77013" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77013-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77013-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77013-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am getting there. It is a paths problem.</p>
<ol>
<li>Place the osmosis folder on the desktop</li>
<li>Place test.osm in the osmosis\bin folder along with osmosis.bat</li>
<li>Create a shortcut for osmosis.bat. r-click &gt; Properties. Add C:\Windows\System32\cmd.exe /k in Target so it reads C:\Windows\System32\cmd.exe /k C:\Users\John\Desktop\Osmosis\bin\osmosis.bat</li>
<li>click the shortcut to run osmosis</li>
<li>type osmosis --read-xml file=Test.osm --write-xml file=fred.osm</li>
</ol>
<p>osmosis runs and fred.osm is written to \bin.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '20, 19:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a99494537d2727b5ac2d5e58ddd6793b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John-Ha&#39;s gravatar image" />
<p><span>John-Ha</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John-Ha has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77013" class="comments-container">
&#10;</div>
<div id="comment-tools-77013" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77013-form-container" class="comment-form-container">
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

