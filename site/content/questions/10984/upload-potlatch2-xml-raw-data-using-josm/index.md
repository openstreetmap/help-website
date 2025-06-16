+++
type = "question"
title = "Upload Potlatch2 XML Raw data using JOSM"
description = '''I&#x27;ve recently got a zero-length way error editing in Potlatch2, so it doesn&#x27;t allow me to upload the changeset. I&#x27;ve found the error so now i have the corrected Potlatch2 code ( &amp;lt;osmchange version=&quot;0.6&quot;&amp;gt;...&amp;lt;/osmchange&amp;gt; ) and i want to upload it. I&#x27;ve heard that is possible using JOSM, bu...'''
date = "2012-03-06T04:05:00Z"
lastmod = "2012-10-19T00:17:00Z"
weight = 10984
keywords = [ "potlatch2", "xml", "upload", "josm" ]
aliases = [ "/questions/10984" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Upload Potlatch2 XML Raw data using JOSM](/questions/10984/upload-potlatch2-xml-raw-data-using-josm)

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
<span id="post-10984-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10984-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-10984-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've recently got a zero-length way error editing in Potlatch2, so it doesn't allow me to upload the changeset. I've found the error so now i have the corrected Potlatch2 code ( &lt;osmchange version="0.6"&gt;...&lt;/osmchange&gt; ) and i want to upload it. I've heard that is possible using JOSM, but I've neved used it and when I try to open de XML file (adding &lt;?xml version='1.0' encoding='UTF-8'?&gt; in the begining) it says "No data found".</p>
<p>Any ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span> <span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Mar '12, 04:05</strong></p>
<img src="https://secure.gravatar.com/avatar/c6bc33c0581c99a2573e8609d145b56a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dintrans_g&#39;s gravatar image" />
<p><span>dintrans_g</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dintrans_g has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-10984" class="comments-container">
&#10;</div>
<div id="comment-tools-10984" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10984-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="11035"></span>

<div id="answer-container-11035" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11035-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11035-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11035-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dintrans_g has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've used <a href="http://svn.openstreetmap.org/applications/utils/import/bulkupload/">upload.py</a> for this with success.</p>
<p>Don't forget to post a trac ticket if you know how the 0-length way was created, so the Potlatch developers can fix it. :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Mar '12, 11:05</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-11035" class="comments-container">
&#10;</div>
<div id="comment-tools-11035" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11035-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17009"></span>

<div id="answer-container-17009" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17009-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-17009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please see:</p>
<p><a href="http://addictedtoosm.wordpress.com/2012/10/01/placeholder-relation-not-found-e-agora/">http://addictedtoosm.wordpress.com/2012/10/01/placeholder-relation-not-found-e-agora/</a></p>
<p>It is in Portuguese (use your favorite translator), but the essence is:</p>
<ul>
<li>Click the View Data button in PL2 and copy all the data.</li>
<li>Paste it in your favourite text editor, do not forget to use the UTF-8 format.</li>
<li>Edit the file correcting the mistakes. Be careful with the XML format and character escaping!</li>
<li>Remove all references to the failed changeset from the XML code, in the form of <em>changeset="1234"</em> (Of course "1234" is the ID of your CS and not the number 1234... Take note of your CS#)</li>
<li>Save it as myChange.osc (OSMChange) (or whatever name you prefer)</li>
<li>Open JOSM and open the .osc file</li>
<li>Upload the changes, setting the option of using an existing, open, changeset. Use the Changeset Id you took note before.</li>
</ul>
<p>That's it, worked a few times for me.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '12, 00:17</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-17009" class="comments-container">
&#10;</div>
<div id="comment-tools-17009" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17009-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11032"></span>

<div id="answer-container-11032" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11032-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The page on the .osm file format contains links to various tools for handling, importing, exporting osm xml files:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/.osm">https://wiki.openstreetmap.org/wiki/.osm</a></p>
<p>There may also be something useful to you in here:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/API_v0.6">https://wiki.openstreetmap.org/wiki/API_v0.6</a></p>
<p>(I'm searching for something to support "mechanical edits" myself)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Mar '12, 10:08</strong></p>
<img src="https://secure.gravatar.com/avatar/6f7f371cdb061bf0d289a885af8705cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ViewFromTheBoundary&#39;s gravatar image" />
<p><span>ViewFromTheB...</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ViewFromTheBoundary has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Mar '12, 10:31</strong> </span></p>
</div>
</div>
<div id="comments-container-11032" class="comments-container">
&#10;</div>
<div id="comment-tools-11032" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11032-form-container" class="comment-form-container">
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

