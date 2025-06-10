+++
type = "question"
title = "Can&#x27;t upload .osc to local Rails Port instance."
description = '''I have been experimenting with a local instance of Rails Port. I used osmosis to load a small pbf of my neighborhood. Using JOSM I edited some data on the local instance. Then a few weeks later I downloaded the latest osm of my neighborhood. Using osmosis I generated a .osc file, a diff between my p...'''
date = "2017-11-21T11:57:00Z"
lastmod = "2017-11-25T09:12:00Z"
weight = 60724
keywords = [ ".osc", "postgresql", "osmosis", "railsport" ]
aliases = [ "/questions/60724" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't upload .osc to local Rails Port instance.](/questions/60724/cant-upload-osc-to-local-rails-port-instance)

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
<span id="post-60724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60724-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been experimenting with a local instance of Rails Port. I used <code>osmosis</code> to load a small <code>pbf</code> of my neighborhood. Using JOSM I edited some data on the local instance. Then a few weeks later I downloaded the latest <code>osm</code> of my neighborhood. Using <code>osmosis</code> I generated a <code>.osc</code> file, a diff between my postgres database and the new <code>osm</code> file. I opened the <code>.osc</code> file with <code>JOSM</code> where I could see the changes, but I couldn't upload the changes to local postgres database. It shows a conflict and upon giving sync, both entire data set and specific node it wouldn't upload ans keep showing the same conflict message.</p>
<p>P.S.: yes I have a user account on local Rails Port instance with what I can upload data manually and yes I changed the OSM Server URL to point my local instance which is <a href="http://localhost:3000/api">http://localhost:3000/api</a></p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-.osc" rel="tag" title="see questions tagged &#39;.osc&#39;">.osc</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-railsport" rel="tag" title="see questions tagged &#39;railsport&#39;">railsport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Nov '17, 11:57</strong></p>
<img src="https://secure.gravatar.com/avatar/fa2f470a891d0bee66ec570d0e94868b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sawan%20Shariar&#39;s gravatar image" />
<p><span>Sawan Shariar</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sawan Shariar has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Nov '17, 13:23</strong> </span></p>
</div>
</div>
<div id="comments-container-60724" class="comments-container">
<span id="60725"></span>
<div id="comment-60725" class="comment">
<div id="post-60725-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you really created a diff between your <em>database</em> and the new osm file, or a diff between the old pbf file and the new osm file? -- Could you post the conflict error message?</p>
</div>
<div id="comment-60725-info" class="comment-info">
<span class="comment-age">(21 Nov '17, 12:33)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="60747"></span>
<div id="comment-60747" class="comment">
<div id="post-60747-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes, I created a diff between my database and the new osm file. Error message from JOSM: 'Conflicts detected Uploading failed because the server has a newer version of one of your nodes, ways, or relations. The conflict is caused by the node with id 1,472,108,803, the server has version 1, your version is 2. Click to Synchronize node 1,472,108,803 only to synchronize the conflicting primitive only. Click to Synchronize entire dataset to synchronize the entire local dataset with the server.Click Cancel to abort and continue editing.' If I click on any of them it syncs with the database and gives me the same conflict error.</p>
</div>
<div id="comment-60747-info" class="comment-info">
<span class="comment-age">(23 Nov '17, 13:22)</span> <span class="comment-user userinfo">Sawan Shariar</span>
</div>
</div>
</div>
<div id="comment-tools-60724" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60724-form-container" class="comment-form-container">
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

<span id="60753"></span>

<div id="answer-container-60753" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60753-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The versions of the objects in your .osc have somehow been incremented and no longer match what's in the database. As per <a href="http://wiki.openstreetmap.org/wiki/Elements">Elements</a>:</p>
<p>"Version: Integer - The edit version of the object. Newly created objects start at version 1 and the value is incremented by the server when a client uploads a new version of the object. <strong>The server will reject a new version of an object if the version sent by the client does not match the current version of the object in the database.</strong>"</p>
<p>Once you upload the modified objects with the same version as in the database, the server will then increment the version number for you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Nov '17, 16:57</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-60753" class="comments-container">
<span id="60772"></span>
<div id="comment-60772" class="comment">
<div id="post-60772-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>so how do you suggest I go ahead with the marge?</p>
</div>
<div id="comment-60772-info" class="comment-info">
<span class="comment-age">(25 Nov '17, 09:12)</span> <span class="comment-user userinfo">Sawan Shariar</span>
</div>
</div>
</div>
<div id="comment-tools-60753" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60753-form-container" class="comment-form-container">
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

