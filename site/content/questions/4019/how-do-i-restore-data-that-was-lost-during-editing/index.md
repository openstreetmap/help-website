+++
type = "question"
title = "How do I restore data that was lost during editing?"
description = '''Something went seriously wrong while adding to a relation in josm (nr. 1490807). All nodes and ways were eliminated from the pertinent relation-number. I have just checked in the Relation-Analyser. It is empty of nodes and ways! A change-set from the previous day is available, but would that restore...'''
date = "2011-03-23T19:17:00Z"
lastmod = "2012-01-08T11:44:00Z"
weight = 4019
keywords = [ "josm", "lost-data" ]
aliases = [ "/questions/4019" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How do I restore data that was lost during editing?](/questions/4019/how-do-i-restore-data-that-was-lost-during-editing)

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
<span id="post-4019-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4019-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-4019-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Something went seriously wrong while adding to a relation in josm (nr. 1490807). All nodes and ways were eliminated from the pertinent relation-number. I have just checked in the Relation-Analyser. It is empty of nodes and ways! A change-set from the previous day is available, but would that restore data from even older edits. How can I restore any lost data?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-lost-data" rel="tag" title="see questions tagged &#39;lost-data&#39;">lost-data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Mar '11, 19:17</strong></p>
<img src="https://secure.gravatar.com/avatar/cd4569f9fa1aac11eb6b19d6de309ea6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dcp&#39;s gravatar image" />
<p><span>dcp</span><br />
<span class="score" title="721 reputation points">721</span><span title="37 badges"><span class="badge1">●</span><span class="badgecount">37</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dcp has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '11, 11:53</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-4019" class="comments-container">
&#10;</div>
<div id="comment-tools-4019" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4019-form-container" class="comment-form-container">
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

<span id="4022"></span>

<div id="answer-container-4022" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4022-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4022-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-4022-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need the History (or <a href="http://wiki.openstreetmap.org/wiki/JOSM/Plugins/Reverter">Revert</a>) plug-in for JOSM.</p>
<ul>
<li>First download the relation using <code>File|Download Object</code> ... Choose 'relation' and 1490807.</li>
<li>Next select the object in JOSM, so that it is shown in the selection window.</li>
<li>Now from the History menu choose the only menu option <code>'Revert Changeset'</code> and a dialogue box appears.</li>
<li>Enter the change set number (7640133) found by browsing the relation.</li>
<li>Select the second option <code>'revert selected objects'</code> and OK.</li>
</ul>
<p>At this point your relation in its old state should be shown in the JOSM relation panel. Specifically, as having its members restored. Before uploading this back to OSM, download all the relation members and check that this looks OK.</p>
<p>Once satisfied that everything is in order then upload the restored relation to OSM.</p>
<p>When manipulating relations in JOSM it is a good idea to ensure that all relation members are downloaded.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '11, 19:55</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-4022" class="comments-container">
<span id="4026"></span>
<div id="comment-4026" class="comment">
<div id="post-4026-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the info. I'll try it later.</p>
</div>
<div id="comment-4026-info" class="comment-info">
<span class="comment-age">(23 Mar '11, 20:35)</span> <span class="comment-user userinfo">dcp</span>
</div>
</div>
</div>
<div id="comment-tools-4022" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4022-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4023"></span>

<div id="answer-container-4023" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4023-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-4023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>you should not undo the complete changeset (unless you have checked that also the other contained edits are wrong) but rather <strong>reupload the relation from the previous version</strong>.</p>
<ul>
<li>You can check the current version in the api: <a href="http://www.openstreetmap.org/browse/relation/1490807">http://www.openstreetmap.org/browse/relation/1490807</a> In your case this is 6.</li>
<li>Now get the previous version: <a href="http://api.openstreetmap.org/api/0.6/relation/1490807/5">http://api.openstreetmap.org/api/0.6/relation/1490807/5</a></li>
<li>save it as name.osm to your disk.</li>
<li>Open it in a text editor and add action="modify" to the row where the relation is described. It would then read like this:</li>
</ul>
&lt;relation id="1490807" action="modify" visible="true" timestamp="2011-03-22T18:08:06Z" user="dcp" uid="44221" version="5" changeset="7639471"&gt;
<ul>
<li><p>Now open this file in JOSM and try to upload. You will get a message that the relation was changed in the meantime (indeed, you are trying to upload version5 but there is already version6). Click OK to synchronize the dataset. A conflict is reported. Go to conflicts in JOSM and solve the conflict by taking "your version" into the middle column. <em>You can also undo only parts and choose other parts from "their version" which is the current version of the relation on the server.</em></p></li>
<li><p>Now upload again, it will work.</p></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '11, 20:00</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Mar '11, 23:30</strong> </span></p>
</div>
</div>
<div id="comments-container-4023" class="comments-container">
<span id="4027"></span>
<div id="comment-4027" class="comment">
<div id="post-4027-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the info. I'll try it later.</p>
</div>
<div id="comment-4027-info" class="comment-info">
<span class="comment-age">(23 Mar '11, 20:35)</span> <span class="comment-user userinfo">dcp</span>
</div>
</div>
</div>
<div id="comment-tools-4023" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4023-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9855"></span>

<div id="answer-container-9855" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9855-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The method of dieterdreist works fine, if no ways have been deleted in the meantime.</p>
<p>If that is the case you will get an error in the uplaod giving you the id of the missing element (but not saying that it is missing!).</p>
<ul>
<li>Cancel the uplaod and download all members of the relation.</li>
<li>In the edit panel try to find the offending elements. In my case I tried to recover a cycle route and some highways had been deleted. They showed up in the relation member list as highways with zero nodes.</li>
<li>Now you need to go back at the .osm file and remove all lines that refer to the deleted elements.</li>
<li>Retry with the modified .osm file again</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '12, 11:44</strong></p>
<img src="https://secure.gravatar.com/avatar/0a45ba8bcc4b69a12b3e817afff187e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="voschix&#39;s gravatar image" />
<p><span>voschix</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="voschix has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9855" class="comments-container">
&#10;</div>
<div id="comment-tools-9855" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9855-form-container" class="comment-form-container">
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

