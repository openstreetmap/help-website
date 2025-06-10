+++
type = "question"
title = "JOSM as local editor?"
description = '''Editing local .osm files using JOSM.  When I save the file and try to exit the program, it prompts that &quot;example.osm should be uploaded. Actions to take: Upload&quot;.  Is there any way to tell JOSM that I&#x27;m not using a server, and that saving the .osm file is sufficient?  Setting the server name to blan...'''
date = "2013-08-01T14:05:00Z"
lastmod = "2013-09-15T12:00:00Z"
weight = 24797
keywords = [ "josm" ]
aliases = [ "/questions/24797" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM as local editor?](/questions/24797/josm-as-local-editor)

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
<span id="post-24797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24797-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Editing local .osm files using JOSM.<br />
</p>
<p>When I save the file and try to exit the program, it prompts that "example.osm should be uploaded. Actions to take: Upload".</p>
<p>Is there any way to tell JOSM that I'm not using a server, and that saving the .osm file is sufficient?<br />
</p>
<p>Setting the server name to blank doesn't work (JOSM doesn't even save that setting if you untick "use the default OSM server" without providing an alternative).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Aug '13, 14:05</strong></p>
<img src="https://secure.gravatar.com/avatar/3e44debd67415e7aa7759c83b829be6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OJW&#39;s gravatar image" />
<p><span>OJW</span><br />
<span class="score" title="151 reputation points">151</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OJW has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-24797" class="comments-container">
&#10;</div>
<div id="comment-tools-24797" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24797-form-container" class="comment-form-container">
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

<span id="26357"></span>

<div id="answer-container-26357" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26357-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-26357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you are working on a single file, edit it in any text editor, changing (or adding) <code>upload='false'</code> in the &lt;osm&gt; tag. This way JOSM won't ask you to upload the file, and instead will give a warning if you try to.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '13, 12:00</strong></p>
<img src="https://secure.gravatar.com/avatar/5cbbf1cf884c2145026c237aaed80dde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zverik&#39;s gravatar image" />
<p><span>Zverik</span><br />
<span class="score" title="613 reputation points">613</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zverik has one accepted answer">10%</span></p>
</div>
</div>
<div id="comments-container-26357" class="comments-container">
&#10;</div>
<div id="comment-tools-26357" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26357-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24815"></span>

<div id="answer-container-24815" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24815-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am using JOSM to edit a local .osm file for features on a map that should not be added to the Openstreetmap database.</p>
<p>Pretty easy to open local files, edit them and save them using the "Open" and "Save" or "Save As" options under the file menu.</p>
<p>However JOSM warns me every time I quit the program that I have unsaved changes (even though I've saved them) and its default action is to upload them. I just make sure I click on the "Exit Now" button.</p>
<p>Then when using mapnik to render my customized map I simply specify the local .osm file as the data source for some of the layers. Works out pretty well for things like adding a UTM grid, local nicknames for locations, etc. to my map image.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Aug '13, 23:21</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-24815" class="comments-container">
<span id="25066"></span>
<div id="comment-25066" class="comment">
<div id="post-25066-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Agreed, that it's easy enough to press "Exit now"; however it just looks messy to ignore a warning dialog during routine use.</p>
</div>
<div id="comment-25066-info" class="comment-info">
<span class="comment-age">(08 Aug '13, 10:52)</span> <span class="comment-user userinfo">OJW</span>
</div>
</div>
</div>
<div id="comment-tools-24815" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24815-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24910"></span>

<div id="answer-container-24910" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24910-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-24910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>JOSM knows that you have saved your file locally. You have the choice on both: you can exit with only a save action. But it's true that we should be able to specify that tou are wroking on a local database of your choice, or that you should be able to submit the data to more databases (each one with ots own status) You could do that by using a dummy database API url, such as "local:" followed by nothing (JOSM would ignore completely the database API.), or "file:" followed by nothing (JOSM in that case would allow you to choose a file destination to save a new copy; ideally it should support "svn:" or "git:" to submit a new version in a local version repository). This would require developing an API adapter. Another possibility is simply to install you own local API server, and specify it as the URL. Note however that object ID's are only significant within a single database (you may use another API URL, but this only works because these APIs are connected to the same target database).</p>
<p>We still lack the possibility to manage multiple ID's to perform synchronization between databases. The only mechanism avaliable is the use of "negative" ID's which means that we still don't know the remote ID as it does not exist remotely.</p>
<p>Sync'ing different databases (with their own spaces for their own IDs) is something that JOSM still does not perform: this requires manual preparation and there's no automated tool to link objects from one database to another. and select those that we will correlate. All we can do is to have separate layer worksheets, each one connectd to a single database (with negative IDs for objects still missing in the associated database).</p>
<p>But the UI still does not allow selecting the target database API to associate with a layer worksheet. But ideally all objects loaded in JOSM should be able to store one ID per database, and each database adapter should specidy if it supports ID's from other databases (in OSM, you could associate a custom "ref:&lt;db&gt;=&lt;id&gt;" attribute to objects, and should be able to specify those to discard/ignore on output to the API. These foreign keys should not be retrieved by default, unless the user explicitly requests them. They should be stored in tables separated from other attributes (tag/value)</p>
<p>The OSM API should also facilitate the retrieval of objects using their foreign IDs. In my opinion this should not even be standard attributes/tags but managed in a separate index table as "foreign keys". We could also have adatation profiles indicating how to convert tags from one database to tags for the other database with a set of mapping rules for each adaptation.</p>
<p>The OSM database could store these adapter rules as new kind of objects.</p>
<p>An example of use would be the creation of separzte stores for working collaboratively on some areas or on some kind of objects and occasionally syn them with another target database. This could allow things like perliminary QA checks, collaborative work to prepare merges before imports.</p>
<p>May be someday the API will evolve into a system like Git, where each user has its own store for the data he is working with, and with othe people working in synchronizations (the synchronizations could then become bidirectional)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Aug '13, 08:22</strong></p>
<img src="https://secure.gravatar.com/avatar/b0ac3d0a15ce4f96f0d6b29172fca72a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Verdy_p&#39;s gravatar image" />
<p><span>Verdy_p</span><br />
<span class="score" title="141 reputation points">141</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Verdy_p has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24910" class="comments-container">
<span id="24974"></span>
<div id="comment-24974" class="comment">
<div id="post-24974-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The question is quite basic and not about syncing different databases or the future of the OSM API. Please don't get that distracted in answers.</p>
</div>
<div id="comment-24974-info" class="comment-info">
<span class="comment-age">(06 Aug '13, 12:29)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24910" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24910-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24943"></span>

<div id="answer-container-24943" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24943-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-24943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As far as I know to edit map you have to agree to the license which says that all edits you do, you have to share/upload. And osm and tools are not for making maps for your use only. I hope you're aware of it. Maybe I'm missing the point, I'm still new to all this. If I do, don't mind this post.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Aug '13, 22:58</strong></p>
<img src="https://secure.gravatar.com/avatar/08f475a8bb3c347e3b9860776eacada8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KoyotGamma&#39;s gravatar image" />
<p><span>KoyotGamma</span><br />
<span class="score" title="193 reputation points">193</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KoyotGamma has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-24943" class="comments-container">
<span id="24946"></span>
<div id="comment-24946" class="comment">
<div id="post-24946-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>For info, the OSM Contributor Terms page is <a href="http://www.osmfoundation.org/wiki/License/Contributor_Terms">here</a>. It does NOT say "if you use JOSM, you have to upload the results to OpenStreetMap".<br />
</p>
<p>Information about the licence itself is <a href="http://www.osmfoundation.org/wiki/License">here</a>, but if someone was editing files in an OSM data format that didn't contain data from OpenStreetMap, it wouldn't apply to them.</p>
</div>
<div id="comment-24946-info" class="comment-info">
<span class="comment-age">(05 Aug '13, 23:53)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="24955"></span>
<div id="comment-24955" class="comment">
<div id="post-24955-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The licence (and the contributor terms you have to accept if you want to subbmit data) you see in OSM is definitely about the tools you use to create and submit data. The tools havre their own licences, and OSM does not require you to use any specific tool (approved or nor): JOSM, iD, or other online sites, or even proprietary software are equivaly valid and do not change any term about the content of the OSM database or your use of this database.</p>
</div>
<div id="comment-24955-info" class="comment-info">
<span class="comment-age">(06 Aug '13, 06:11)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="24956"></span>
<div id="comment-24956" class="comment">
<div id="post-24956-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So yes, JOSM is NOT required to upload data ONLY to the OSM database. You could use it to connect to any other database (even a proprietary one). The existing licence of JOSM does not apply to the data you load, create, modify or submit with it. And JOSM can still be extended to support new develoment to connectto multiple databases in the same work session, with multiple layers, and facilities to perform merges with licence tracking for merged data (but you, as a user, must still respect the licences applicable to each public database you'll connect to, if it is not yours.</p>
</div>
<div id="comment-24956-info" class="comment-info">
<span class="comment-age">(06 Aug '13, 06:12)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="24958"></span>
<div id="comment-24958" class="comment">
<div id="post-24958-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So the OSM database can be freely used with JOSM, or QGIS, or AutoCAD, or any other software you create yourself or buy, or pay to be developed specifically for your needs You won't find the term "JOSM" in the OSM licence or in the OSM contributor terms. They are fully independant.</p>
</div>
<div id="comment-24958-info" class="comment-info">
<span class="comment-age">(06 Aug '13, 06:15)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="25065"></span>
<div id="comment-25065" class="comment">
<div id="post-25065-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No database in use here - JOSM is editing a file.<br />
</p>
<p>And yes, OSM tools' licenses typically include 'Freedom 0' ("The freedom to run the program for any purpose").</p>
</div>
<div id="comment-25065-info" class="comment-info">
<span class="comment-age">(08 Aug '13, 10:49)</span> <span class="comment-user userinfo">OJW</span>
</div>
</div>
</div>
<div id="comment-tools-24943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24943-form-container" class="comment-form-container">
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

