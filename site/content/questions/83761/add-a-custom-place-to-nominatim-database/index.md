+++
type = "question"
title = "Add a custom place to Nominatim database"
description = '''I have set up my local Nominatim instance using the mediagis/nominatim:4.0 Docker image and so far so good, it works like a charm. Now, I would like to know if it is possible to add some custom place to the Nominatim database and have them considered in search, lookup, etc. By digging a bit into the...'''
date = "2022-03-09T10:36:00Z"
lastmod = "2023-03-02T09:18:00Z"
weight = 83761
keywords = [ "nominatim", "custom" ]
aliases = [ "/questions/83761" ]
osqa_answers = 6
osqa_accepted = false
+++

<div class="headNormal">

# [Add a custom place to Nominatim database](/questions/83761/add-a-custom-place-to-nominatim-database)

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
<span id="post-83761-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83761-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83761-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have set up my local Nominatim instance using the mediagis/nominatim:4.0 Docker image and so far so good, it works like a charm. Now, I would like to know if it is possible to add some custom place to the Nominatim database and have them considered in search, lookup, etc. By digging a bit into the Nominatim documentation and source code, it seems to me that it should be possible by adding a custom row to the placex table with indexed_status != 0. It looks like there is also the possibility of using "osm_type = X" for e"X"ternal sources. So I ask: will just adding a row to the placex table trigger everything is needed to have that custom place considered in the various Nominatim functionalities? And, in case, what are the columns to be filled for that to work? Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Mar '22, 10:36</strong></p>
<img src="https://secure.gravatar.com/avatar/7f376eb35f20c1f021067ede20bd4e6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="todelo&#39;s gravatar image" />
<p><span>todelo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="todelo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83761" class="comments-container">
&#10;</div>
<div id="comment-tools-83761" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83761-form-container" class="comment-form-container">
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

6 Answers:

</div>

</div>

<span id="83778"></span>

<div id="answer-container-83778" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83778-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-83778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The e"X"ternal data feature is a piece of very old unmaintained code that likely won't really do what you want. Most importantly, it won't add your data to the search tables, so you can't really find it.</p>
<p>The easiest way to add custom data to Nominatim is to convert your data into OSM format and then add it with <code>nominatim add-data --file &lt;custom.xml&gt;</code> followed by an indexing <code>nominatim index</code>. Make sure to use OSM IDs that are not yet in the database. This way you can be sure that address computation and building of the search index are handled just as for any other data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Mar '22, 07:51</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-83778" class="comments-container">
<span id="83781"></span>
<div id="comment-83781" class="comment">
<div id="post-83781-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Then Nominatim interprets it as an update and replaces your data.</p>
</div>
<div id="comment-83781-info" class="comment-info">
<span class="comment-age">(10 Mar '22, 09:08)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="83782"></span>
<div id="comment-83782" class="comment">
<div id="post-83782-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Indeed. Is there a way to prevent this? Is a meaningful OSM_ID really needed for search and lookup?</p>
</div>
<div id="comment-83782-info" class="comment-info">
<span class="comment-age">(10 Mar '22, 09:18)</span> <span class="comment-user userinfo">todelo</span>
</div>
</div>
</div>
<div id="comment-tools-83778" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83778-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83780"></span>

<div id="answer-container-83780" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83780-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83780-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83780-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I see. But what happens if I update my database with an extract of the updated OSM data and the OSM_IDs I've chosen get duplicated?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Mar '22, 09:00</strong></p>
<img src="https://secure.gravatar.com/avatar/7f376eb35f20c1f021067ede20bd4e6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="todelo&#39;s gravatar image" />
<p><span>todelo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="todelo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Mar '22, 09:01</strong> </span></p>
</div>
</div>
<div id="comments-container-83780" class="comments-container">
&#10;</div>
<div id="comment-tools-83780" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83780-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84430"></span>

<div id="answer-container-84430" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84430-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After a few months not working on the problem I tried Ionvia's solution, but something did not work. I created an xml file from a DataFrame with pyosmium. The file looks like this:</p>
<p><img src="https://help.openstreetmap.org/upfiles/Screenshot_from_2022-05-10_17-37-12.png" alt="alt text" /></p>
<p>I run <code>nominatim add-data --file &lt;myfile.xml&gt;</code> and the nodes indeed appear in the <code>planet_osm_nodes</code> table. However, the command <code>nominatim index</code> runs with no errors but indexes <code>0/0</code> new objects at every rank level. And indeed the new nodes do not eventually appear in the <code>placex</code> table and therefore do not show up in the <code>search</code>.</p>
<p>What am I missing?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 May '22, 16:35</strong></p>
<img src="https://secure.gravatar.com/avatar/7f376eb35f20c1f021067ede20bd4e6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="todelo&#39;s gravatar image" />
<p><span>todelo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="todelo has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 May '22, 16:37</strong> </span></p>
</div>
</div>
<div id="comments-container-84430" class="comments-container">
<span id="84431"></span>
<div id="comment-84431" class="comment">
<div id="post-84431-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's <code>addr:housenumber</code> not <code>addr:house_number</code>.</p>
</div>
<div id="comment-84431-info" class="comment-info">
<span class="comment-age">(10 May '22, 16:55)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="84433"></span>
<div id="comment-84433" class="comment">
<div id="post-84433-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh dear! Thank you so much!</p>
</div>
<div id="comment-84433-info" class="comment-info">
<span class="comment-age">(10 May '22, 21:37)</span> <span class="comment-user userinfo">todelo</span>
</div>
</div>
</div>
<div id="comment-tools-84430" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84430-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86831"></span>

<div id="answer-container-86831" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86831-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi <a href="https://help.openstreetmap.org/users/21498/todelo">@todelo</a> I need to edit the column 'extratags' in the table 'placex'. I have installed Nominatim in my local machine. Its possible to make this changes in the database?</p>
<p>Could you help me with this?</p>
<p>Thank you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '23, 15:32</strong></p>
<img src="https://secure.gravatar.com/avatar/88d43a2ecb5b0fc62a4db7f97a166682?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Martim&#39;s gravatar image" />
<p><span>Martim</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Martim has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86831" class="comments-container">
&#10;</div>
<div id="comment-tools-86831" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86831-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86832"></span>

<div id="answer-container-86832" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86832-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86832-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86832-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi <a href="https://help.openstreetmap.org/users/21498/todelo">@todelo</a> I need to edit the column 'extratags' in the table 'placex'. I have installed Nominatim in my local machine. Its possible to make this changes in the database?</p>
<p>Could you help me with this?</p>
<p>Thank you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '23, 15:32</strong></p>
<img src="https://secure.gravatar.com/avatar/88d43a2ecb5b0fc62a4db7f97a166682?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Martim&#39;s gravatar image" />
<p><span>Martim</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Martim has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86832" class="comments-container">
&#10;</div>
<div id="comment-tools-86832" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86832-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86837"></span>

<div id="answer-container-86837" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86837-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86837-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86837-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What do you mean exactly? If you have your local installation, that means you have a local postgreSQL database, so you can modify the extratags column with standard SQL commands. I am not sure what happens to your changes if you update your data though</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Mar '23, 09:18</strong></p>
<img src="https://secure.gravatar.com/avatar/7f376eb35f20c1f021067ede20bd4e6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="todelo&#39;s gravatar image" />
<p><span>todelo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="todelo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86837" class="comments-container">
&#10;</div>
<div id="comment-tools-86837" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86837-form-container" class="comment-form-container">
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

