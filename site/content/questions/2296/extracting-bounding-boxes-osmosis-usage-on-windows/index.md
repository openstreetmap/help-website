+++
type = "question"
title = "Extracting bounding boxes - Osmosis usage on Windows"
description = '''Hello I have downloaded europe.osm.bz2 and I would like to exctract a large area using osmosis. Please forgive me for my ignorance, I am not a Linux / Unix at all and if I am missing something obvious, please advise. I am ammending this script I found on the https://wiki.openstreetmap.org/wiki/Osmosi...'''
date = "2011-01-19T13:47:00Z"
lastmod = "2012-05-24T00:49:00Z"
weight = 2296
keywords = [ "windows", "osmosis" ]
aliases = [ "/questions/2296" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting bounding boxes - Osmosis usage on Windows](/questions/2296/extracting-bounding-boxes-osmosis-usage-on-windows)

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
<span id="post-2296-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2296-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2296-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello I have downloaded europe.osm.bz2 and I would like to exctract a large area using osmosis. Please forgive me for my ignorance, I am not a Linux / Unix at all and if I am missing something obvious, please advise.</p>
<p>I am ammending this script I found on the <a href="https://wiki.openstreetmap.org/wiki/Osmosis#Extracting_bounding_boxes"></a><a href="https://wiki.openstreetmap.org/wiki/Osmosis#Extracting_bounding_boxes"></a><a href="https://wiki.openstreetmap.org/wiki/Osmosis#Extracting_bounding_boxes">https://wiki.openstreetmap.org/wiki/Osmosis#Extracting_bounding_boxes</a>.</p>
<p>Published script:</p>
<pre><code> bzcat downloaded.osm.bz2 | osmosis\
  --read-xml enableDateParsing=no file=/dev/stdin\
  --bounding-box top=49.5138 left=10.9351 bottom=49.3866 right=11.201 --write-xml file=-\
  | bzip2 &gt; extracted.osm.bz2</code></pre>
<p>My ammended script:</p>
<pre><code> bzcat.exe &quot;I:\europe.osm.bz2&quot; | osmosis.bat\
  --read-xml enableDateParsing=no file=CONIN$\
  --bounding-box top=51.2 left=11.7 bottom=47.6 right=23.0 --write-xml file=-\
  | bzip2 &gt; &quot;I:\czechoslovakia.osm.bz2&quot;</code></pre>
<p>Quite frankly I do not even know what the symbol really stands for and if it necessary on windows. I am assuming the | is some pipeline notification.</p>
<p>Here is what I am getting back.</p>
<p>bzcat.exe: I/O or other error, bailing out. Possible reason follows. bzcat.exe: Invalid argument Input file = I:europe.osm.bz2, output file = (stdout)</p>
<p>C:Mapyosmosis-0.38bin&gt;--read-xml enableDateParsing=no file=CONIN$ '--read-xml' is not recognized as an internal or external command, operable program or batch file.</p>
<p>C:Mapyosmosis-0.38bin&gt;--bounding-box top=51.2 left=11.7 bottom=47.6 right=23.0 --write-xml file=- '--bounding-box' is not recognized as an internal or external command, operable program or batch file. | was unexpected at this time.</p>
<p>Please advise.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jan '11, 13:47</strong></p>
<img src="https://secure.gravatar.com/avatar/bbe97c3fa23d557d5cdaec1fef8e28db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tomas%20Pajonk&#39;s gravatar image" />
<p><span>Tomas Pajonk</span><br />
<span class="score" title="191 reputation points">191</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tomas Pajonk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2296" class="comments-container">
&#10;</div>
<div id="comment-tools-2296" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2296-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="2334"></span>

<div id="answer-container-2334" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2334-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2334-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2334-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems like you need to write everything on one line (or something). This is an error from DOS/Windows:</p>
<pre><code> &#39;--bounding-box&#39; is not recognized as an internal or external command, operable program or batch file. | was unexpected at this time.</code></pre>
<p>Also I think you forgot the last pipe, try to just export to OSM (or pbf) and see if that works, so write it like this:</p>
<pre><code>bzcat.exe &quot;I:\europe.osm.bz2&quot; | osmosis.bat --read-xml enableDateParsing=no file=CONIN$  --bounding-box top=51.2 left=11.7 bottom=47.6 right=23.0 --write-xml file=&quot;I:\czechoslovakia.osm&quot;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jan '11, 22:01</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jan '11, 22:34</strong> </span></p>
</div>
</div>
<div id="comments-container-2334" class="comments-container">
<span id="4064"></span>
<div id="comment-4064" class="comment">
<div id="post-4064-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why is bzcat used? I thought Osmosis could read .bz2 files anyway?</p>
</div>
<div id="comment-4064-info" class="comment-info">
<span class="comment-age">(25 Mar '11, 10:02)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="4237"></span>
<div id="comment-4237" class="comment">
<div id="post-4237-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>running gz/bz2 as a separate task doesn't hurt and the Java implementations have been known to be buggy (e.g. java had/have problems with gzip concatenated streams).</p>
</div>
<div id="comment-4237-info" class="comment-info">
<span class="comment-age">(31 Mar '11, 21:11)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
</div>
<div id="comment-tools-2334" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2334-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4061"></span>

<div id="answer-container-4061" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4061-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4061-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4061-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Instead of file=CONIN$ you have to use file"-" (see <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailedklzzwxh:0000Usageklzzwxh:00010.39">https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.39</a>)</p>
<p>In my example i used 7-zip (bzcat should work as well when using -d -c as parameters)</p>
<p>c:Programme7-Zip7z.exe e -so I:AdminThomasosmxmleurope.osm.bz2 | D:OSMosmosisbinosmosis.bat --rx file="-" --tf accept-ways highway=motorway,trunk,primary --used-node --write-xml file="I:AdminThomasosmxmleuropa_einfach_highway.osm"</p>
<p>This extracts motorway, trunk and primary street from europe</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '11, 08:32</strong></p>
<img src="https://secure.gravatar.com/avatar/dbc04706922ab4f5f4bb5cf6e35e8c73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tmandel&#39;s gravatar image" />
<p><span>tmandel</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tmandel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4061" class="comments-container">
&#10;</div>
<div id="comment-tools-4061" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4061-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2297"></span>

<div id="answer-container-2297" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2297-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2297-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-2297-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>All that I can reliably tell from that error message is that bzcat.exe (not osmosis) is unhappy. So this is not directly openstreetmap related. Check the documentation if the input filename should be I:/europe.osm.bz2 rather than I:europe.osm.bz2.</p>
<p>Also you might have to use bzip2.exe instead of bzip, but that is unrelated as it breaks down before it ever reaches that stage.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jan '11, 13:55</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-2297" class="comments-container">
<span id="2298"></span>
<div id="comment-2298" class="comment">
<div id="post-2298-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When I supplied an incorect file name the error message was different.</p>
</div>
<div id="comment-2298-info" class="comment-info">
<span class="comment-age">(19 Jan '11, 14:08)</span> <span class="comment-user userinfo">Tomas Pajonk</span>
</div>
</div>
<span id="2299"></span>
<div id="comment-2299" class="comment">
<div id="post-2299-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I made a wrong call with the bzcat.exe. I should have called just bzcat.</p>
</div>
<div id="comment-2299-info" class="comment-info">
<span class="comment-age">(19 Jan '11, 14:09)</span> <span class="comment-user userinfo">Tomas Pajonk</span>
</div>
</div>
<span id="2300"></span>
<div id="comment-2300" class="comment">
<div id="post-2300-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd also recommend using europe.osm.pbf instead of .bz2, it's probably much faster to process by osmosis.</p>
</div>
<div id="comment-2300-info" class="comment-info">
<span class="comment-age">(19 Jan '11, 14:33)</span> <span class="comment-user userinfo">Breki</span>
</div>
</div>
<span id="2301"></span>
<div id="comment-2301" class="comment">
<div id="post-2301-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Would I then use Osmosis directly on the pbf or do I have to extract it somehow ?</p>
</div>
<div id="comment-2301-info" class="comment-info">
<span class="comment-age">(19 Jan '11, 14:50)</span> <span class="comment-user userinfo">Tomas Pajonk</span>
</div>
</div>
<span id="2305"></span>
<div id="comment-2305" class="comment">
<div id="post-2305-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Directly: <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.37#PBF_Binary_Tasks">https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.37#PBF_Binary_Tasks</a></p>
</div>
<div id="comment-2305-info" class="comment-info">
<span class="comment-age">(19 Jan '11, 17:35)</span> <span class="comment-user userinfo">Breki</span>
</div>
</div>
</div>
<div id="comment-tools-2297" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2297-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12919"></span>

<div id="answer-container-12919" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12919-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Since this is more than a year old, I assume it is answered or not a problem. I agree however that the main problem is a Windows problem with the command syntax. For one thing, Windows commands cannot be continued.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '12, 00:49</strong></p>
<img src="https://secure.gravatar.com/avatar/969f41ac9bc38a1aea77cd2372daa7e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sam%20Hobbs&#39;s gravatar image" />
<p><span>Sam Hobbs</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sam Hobbs has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12919" class="comments-container">
&#10;</div>
<div id="comment-tools-12919" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12919-form-container" class="comment-form-container">
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

