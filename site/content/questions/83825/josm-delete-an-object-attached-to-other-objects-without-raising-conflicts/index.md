+++
type = "question"
title = "JOSM - Delete an object attached to other objects without raising conflicts?"
description = '''Hi I want to delete a long linear way. I know it&#x27;s id so I download just that object.  It&#x27;s attached to other objects, so JOSM throws conflict errors &amp;amp; insists that the offending objects are also downloaded and then the user can decide if they want to keep them. Due to it being a long object, JO...'''
date = "2022-03-12T23:45:00Z"
lastmod = "2022-06-24T22:29:00Z"
weight = 83825
keywords = [ "conflicts", "josm", "shared_nodes", "delete" ]
aliases = [ "/questions/83825" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM - Delete an object attached to other objects without raising conflicts?](/questions/83825/josm-delete-an-object-attached-to-other-objects-without-raising-conflicts)

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
<span id="post-83825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83825-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I want to delete a long linear way. I know it's id so I download just that object.</p>
<p>It's attached to other objects, so JOSM throws conflict errors &amp; insists that the offending objects are also downloaded and then the user can decide if they want to keep them. Due to it being a long object, JOSM doesn't allow all the data to be d/l in one go. This is frustrating. Is there a way to tell JOSM to default to retaining all the nodes of the other objects?</p>
<p>In Potlach there's never a problem, it deletes the linear object &amp; automatically keeps the previously shared nodes.</p>
<p>I'm struggling to see a scenario when a node that's still in use by another object would want to be deleted.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-conflicts" rel="tag" title="see questions tagged &#39;conflicts&#39;">conflicts</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-shared_nodes" rel="tag" title="see questions tagged &#39;shared_nodes&#39;">shared_nodes</span> <span class="post-tag tag-link-delete" rel="tag" title="see questions tagged &#39;delete&#39;">delete</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Mar '22, 23:45</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-83825" class="comments-container">
<span id="83838"></span>
<div id="comment-83838" class="comment">
<div id="post-83838-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi</p>
<blockquote>
<p>I'm struggling to see a scenario when a node that's still in use by another object would want to be deleted.</p>
</blockquote>
<p>It depends on the types of objects I guess, but for example when two buildings were attached, and you delete one, if the common nodes were not the corners of the remaining one, I would delete them. Nodes along a straight way are useless, and sometimes even confusing IMHO.</p>
<p>The same can happen with roads I think. A simple rule could, if removing the (untagged of course) node from the remaining object doesn't change its geometry, then let's delete it !</p>
<p>My 2 cents.</p>
</div>
<div id="comment-83838-info" class="comment-info">
<span class="comment-age">(13 Mar '22, 17:41)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-83825" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83825-form-container" class="comment-form-container">
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

<span id="83830"></span>

<div id="answer-container-83830" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83830-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's a "download along" tool that will allow you to download all objects within a certain distance of an object. I can't remember whether this built in or a plugin. Once all of the nodes are withing download regions I think it should automatically retain shared nodes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '22, 12:58</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-83830" class="comments-container">
<span id="83839"></span>
<div id="comment-83839" class="comment">
<div id="post-83839-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's been part of the core for some time now. Here is the <a href="https://josm.openstreetmap.de/wiki/Help/Action/DownloadAlongWay">doc</a> about it. But it's only based on distance. Based on the question, it would be best to download only the connected objects. Because choosing the right distance might prove tricky.</p>
</div>
<div id="comment-83839-info" class="comment-info">
<span class="comment-age">(13 Mar '22, 17:45)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-83830" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83830-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83832"></span>

<div id="answer-container-83832" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83832-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83832-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83832-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think you can instruct JOSM to download all parent objects of what you have selected, which would get you the other objects referencing your way, and therefore - in a similar way as stated by InsertUser - not remove those nodes still required for those other ways.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '22, 14:31</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-83832" class="comments-container">
<span id="83840"></span>
<div id="comment-83840" class="comment">
<div id="post-83840-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If I understand the <a href="https://josm.openstreetmap.de/wiki/Help/Action/DownloadObject">doc</a> correctly, and you are indeed talking about this "Download object" with referrers functionnality, it is meant for ways and relations. You can't download ways that are connected via nodes with it.</p>
</div>
<div id="comment-83840-info" class="comment-info">
<span class="comment-age">(13 Mar '22, 17:48)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="83841"></span>
<div id="comment-83841" class="comment">
<div id="post-83841-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My bad, reading that <a href="https://josm.openstreetmap.de/ticket/5293">bug report</a>, it seems if you download the nodes with this, you'll get all the referencing ways... But you would have to specify all the nodes, if it's a really long way, with lots of nodes, this can get cumbersome...</p>
</div>
<div id="comment-83841-info" class="comment-info">
<span class="comment-age">(13 Mar '22, 17:52)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="83842"></span>
<div id="comment-83842" class="comment">
<div id="post-83842-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think he means select all and use <a href="https://josm.openstreetmap.de/wiki/Help/Action/DownloadParentWaysAndRelation">Download Parent Ways And Relation</a>. Although I suspect JOSM would warn anyway.</p>
</div>
<div id="comment-83842-info" class="comment-info">
<span class="comment-age">(13 Mar '22, 17:53)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="83844"></span>
<div id="comment-83844" class="comment">
<div id="post-83844-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/4426/insertuser">@InsertUser</a> well it makes sense, if you download the way, select all its nodes, hit Ctrl+Alt+D and then delete the way, it should be good, no ?</p>
<p>There will be a warning about working in an undownloaded area, but there should be no conflict, I think.</p>
</div>
<div id="comment-83844-info" class="comment-info">
<span class="comment-age">(13 Mar '22, 18:33)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-83832" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83832-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83843"></span>

<div id="answer-container-83843" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83843-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi</p>
<p>As the others, I can't answer your original question about an option to just let the nodes be.</p>
<p>But here is an <a href="http://overpass-turbo.eu/?Q=%5Bout%3Ajson%5D%5Btimeout%3A25%5D%3B%0A%0Away(913690987)%3B%0A%0A%3E%3B%0A%3C%3B%0Aout%20body%3B%0A%3E%3B%0Aout%20skel%20qt%3B">overpass query</a>, that loads all intersecting ways, to a specified one. The result is quite big, because this ferry line intersect the Irish boundaries and coastline, but that's just an example ! ;-)</p>
<p>You can refine this query to your need, even filtering by type of way (or maybe only ways and not relations), then you can use <a href="https://josm.openstreetmap.de/wiki/Help/Action/Download#DownloadfromOverpassAPI">JOSM download from overpass</a> functionality.</p>
<p>Hope this helps.</p>
<p>Best regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '22, 18:29</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-83843" class="comments-container">
&#10;</div>
<div id="comment-tools-83843" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83843-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84878"></span>

<div id="answer-container-84878" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84878-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If understand question correctly. Example: massive (BS object) landuse=farmland connected to roads forest etc. want shrink (delete) it and draw 50 proper farmland, grassland etc., but do not want to download whole area with 100k nodes just avoid deleting nodes connected to it. Safely unglue (G) it.</p>
<p>Select way. Using plugin 'utilsplugin2' or can be done with search (Ctrl-F) and 'child selected'. Selection &gt; Select way nodes (Ctrl+Shif-N) Shift select way too in case. Edit &gt; Copy (Ctrl-C). File &gt; Download object... Object type: mixed | Object ID: should be there after Copy. Download objects.</p>
<p>I don't know if it will help and only solution working in JOSM for me. Maybe exist simple "one-click" solution, I can't find any. Other suggestion/tools don't work, atleast for me.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '22, 22:29</strong></p>
<img src="https://secure.gravatar.com/avatar/5decb877d79dbcb50a7ee4770280359f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mindedie&#39;s gravatar image" />
<p><span>mindedie</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mindedie has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jun '22, 22:43</strong> </span></p>
</div>
</div>
<div id="comments-container-84878" class="comments-container">
&#10;</div>
<div id="comment-tools-84878" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84878-form-container" class="comment-form-container">
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

