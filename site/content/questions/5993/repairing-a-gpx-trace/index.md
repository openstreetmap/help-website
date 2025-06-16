+++
type = "question"
title = "Repairing a GPX Trace"
description = '''Today did a 9 mile walk and a lots of route as not been mapped into OSM. For some reason my garmin trace as a problem it won&#x27;t open with my downloading software (memory map) it looks ok in a text editor, much like the dozens I&#x27;ve uploaded before,I tried memory card down load as well no luck. I have ...'''
date = "2011-06-26T00:43:00Z"
lastmod = "2016-12-23T00:57:00Z"
weight = 5993
keywords = [ "edit", "repair", "gpx", "trace" ]
aliases = [ "/questions/5993" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Repairing a GPX Trace](/questions/5993/repairing-a-gpx-trace)

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
<span id="post-5993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5993-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Today did a 9 mile walk and a lots of route as not been mapped into OSM. For some reason my garmin trace as a problem it won't open with my downloading software (memory map) it looks ok in a text editor, much like the dozens I've uploaded before,I tried memory card down load as well no luck. I have linux and windows available what could I chop or clean up this with and save as a GPX it was a nice walk but don't want to go there again for a while. I can use bing to map some but that is not ideal.any ideas</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-edit" rel="tag" title="see questions tagged &#39;edit&#39;">edit</span> <span class="post-tag tag-link-repair" rel="tag" title="see questions tagged &#39;repair&#39;">repair</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-trace" rel="tag" title="see questions tagged &#39;trace&#39;">trace</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '11, 00:43</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Aug '14, 08:49</strong> </span></p>
</div>
</div>
<div id="comments-container-5993" class="comments-container">
<span id="5994"></span>
<div id="comment-5994" class="comment">
<div id="post-5994-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>note the file does have usual list of lat lons and time stamps</p>
</div>
<div id="comment-5994-info" class="comment-info">
<span class="comment-age">(26 Jun '11, 00:45)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-5993" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5993-form-container" class="comment-form-container">
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

<span id="6004"></span>

<div id="answer-container-6004" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6004-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-6004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="andy mackey has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"Not well-formed (invalid token)" sounds like there's something in the XML that shouldn't be there.</p>
<p>I'd suggest you run the file through an online XML validator, such as <a href="http://www.validome.org/xml/">this one</a>. If there's a problem with the XML, it will tell you what it is.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '11, 12:11</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-6004" class="comments-container">
<span id="6013"></span>
<div id="comment-6013" class="comment">
<div id="post-6013-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Richard your link was so easy to use found the same faulty line as foxe but more detail.I edited to make it look like other lines' syntax in Notepad++ but then struggled to change file extension back from TXT to GPX. the file now opens ok and I will upload it tomorrow.very pleased thought i may have lost the trace.thanks also to Vclaw</p>
</div>
<div id="comment-6013-info" class="comment-info">
<span class="comment-age">(26 Jun '11, 16:47)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="53675"></span>
<div id="comment-53675" class="comment">
<div id="post-53675-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Richard that link doesn't work at the moment</p>
</div>
<div id="comment-53675-info" class="comment-info">
<span class="comment-age">(22 Dec '16, 23:40)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="53676"></span>
<div id="comment-53676" class="comment">
<div id="post-53676-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/644/andy-mackey"></a><a href="https://help.openstreetmap.org/users/644/andy-mackey">@andy mackey</a>: according to the <a href="http://wayback.archive.org/web/20150807041932/http://www.validome.org/xml/">Internet Archive's snapshot</a> it is down since about Sept. 2015.</p>
<p>Instead, I would suggest to use the <span>W3C Markup Validator</span>.</p>
</div>
<div id="comment-53676-info" class="comment-info">
<span class="comment-age">(23 Dec '16, 00:24)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="53677"></span>
<div id="comment-53677" class="comment">
<div id="post-53677-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, aseerel4c26 i have just worked out why todays trace wouldn't work see new answer</p>
</div>
<div id="comment-53677-info" class="comment-info">
<span class="comment-age">(23 Dec '16, 00:39)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-6004" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6004-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5996"></span>

<div id="answer-container-5996" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5996-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-5996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have you tried uploading the GPX to <a href="http://openstreetmap.org">openstreetmap.org</a>? Does it work, or does it give any sort of error?</p>
<p>Or you could try opening the GPX file in JOSM (without uploading it). If that works, you can then trace the path etc to add it to the map.</p>
<p>If these don't work, to try and fix the GPX you could:</p>
<ul>
<li><p>Process it using GPXBabel. ie set the input and output formats to GPX, this might fix it.</p></li>
<li><p>Open it in an XML editor. <a href="http://www.firstobject.com/dn_editor.htm">Foxe</a> is a good free option for Windows. This has syntax highlighting, so it should make it easier to spot any errors in the tags. It has an option to validate the file, which should warn of any errors in it.</p></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '11, 02:41</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-5996" class="comments-container">
<span id="5998"></span>
<div id="comment-5998" class="comment">
<div id="post-5998-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Vclaw I'll try your suggestions and report back</p>
</div>
<div id="comment-5998-info" class="comment-info">
<span class="comment-age">(26 Jun '11, 06:25)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="5999"></span>
<div id="comment-5999" class="comment">
<div id="post-5999-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>this is what babel returned..... gpsbabel -w -r -t -i gpx -f C:/Documents and Settings/Compaq_Owner/My Documents/AA GPX TRACKS/AA newest file/20110625.gpx -o gpx -F C:/Documents and Settings/Compaq_Owner/barnwell.gpx -o gpx -F C:/DOCUME~1/COMPAQ~1/LOCALS~1/Temp/qt_temp.Hp3396 GPX: XML parse error at line 31228 of 'C:/Documents and Settings/Compaq_Owner/My Documents/AA GPX TRACKS/AA newest file/20110625.gpx' : not well-formed (invalid token)</p>
<p>Error running gpsbabel: Process exited unsucessfully with code 1</p>
</div>
<div id="comment-5999-info" class="comment-info">
<span class="comment-age">(26 Jun '11, 06:43)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="6000"></span>
<div id="comment-6000" class="comment">
<div id="post-6000-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>josm loaded part of file</p>
</div>
<div id="comment-6000-info" class="comment-info">
<span class="comment-age">(26 Jun '11, 06:46)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="6011"></span>
<div id="comment-6011" class="comment">
<div id="post-6011-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>found foxe a little awkward if I had tried harder I'm sure it would have done it</p>
</div>
<div id="comment-6011-info" class="comment-info">
<span class="comment-age">(26 Jun '11, 16:35)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="6378"></span>
<div id="comment-6378" class="comment">
<div id="post-6378-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If I load a trace from switched on gps it can be a problem (as its still active)from a memory card it works better as its switched off</p>
</div>
<div id="comment-6378-info" class="comment-info">
<span class="comment-age">(17 Jul '11, 11:28)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-5996" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5996-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53678"></span>

<div id="answer-container-53678" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53678-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I just experienced a problem with a trace i couldn't open with my usual programmes. I then notice the memory on my Garmin Oregon's <em>memory was full</em> and it had stopped recording mid location. i should have saved and deleted stuff. I eventually opened the <em>incomplete file</em> with Notepad a text editor, i compared it with a good one, the last sentence was incomplete so i cut and <em>pasted a good ending</em>. so it ended like this:</p>
<pre><code>&lt;trkpt lat=&quot;52.0698085341&quot; lon=&quot;-0.1248275572&quot;&gt;&lt;/trkpt&gt;
&lt;/trkseg&gt;
&lt;/trk&gt;
&lt;/gpx&gt;</code></pre>
<p>saved it and then it worked, apart from the fact the point was from a previous walk of course several KM away.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Dec '16, 00:57</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Dec '16, 01:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-53678" class="comments-container">
&#10;</div>
<div id="comment-tools-53678" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53678-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7157"></span>

<div id="answer-container-7157" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7157-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can also use <a href="http://www.liquid-technologies.com/xml-editor.aspx">Liquid XML Editor</a> to validate your xml file, its not free but then you get a much more fluid UI and syntax highlighting.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '11, 13:48</strong></p>
<img src="https://secure.gravatar.com/avatar/bc4a4317772974b04a430f2307df4013?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael%20Dupre&#39;s gravatar image" />
<p><span>Michael Dupre</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael Dupre has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7157" class="comments-container">
&#10;</div>
<div id="comment-tools-7157" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7157-form-container" class="comment-form-container">
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

