+++
type = "question"
title = "Newbie question: How to &quot;fill&quot; and island with forest"
description = '''Hi fellow osmmappers, So far I have always used iD to map small parts here and there in OSM and it worked nicely for me. Now I was on an island in the Stockholm archipelago and I used my traces and other sources to improve the mapping. This I could do in iD. But now I&#x27;d like to add the fact that thi...'''
date = "2018-08-27T14:03:00Z"
lastmod = "2022-12-30T21:48:00Z"
weight = 65577
keywords = [ "ideditor", "islands", "josm", "forest", "multipolygon" ]
aliases = [ "/questions/65577" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Newbie question: How to "fill" and island with forest](/questions/65577/newbie-question-how-to-fill-and-island-with-forest)

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
<span id="post-65577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65577-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi fellow osmmappers,</p>
<p>So far I have always used iD to map small parts here and there in OSM and it worked nicely for me. Now I was on an <a href="https://www.openstreetmap.org/#map=14/59.4221/18.8842">island in the Stockholm archipelago</a> and I used my traces and other sources to improve the mapping. This I could do in iD.</p>
<p>But now I'd like to add the fact that this island is mostly forest. To map this I would go crazy in iD. So I tried JOSM but it's not really self-explanatory on how I can easily add forest to this island.</p>
<p>Can someone point me to a good tutorial or documentation on how to do this in an efficient way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-islands" rel="tag" title="see questions tagged &#39;islands&#39;">islands</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-forest" rel="tag" title="see questions tagged &#39;forest&#39;">forest</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Aug '18, 14:03</strong></p>
<img src="https://secure.gravatar.com/avatar/eda62d5757720e9bdea819bc7430b49c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="novabeat&#39;s gravatar image" />
<p><span>novabeat</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="novabeat has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65577" class="comments-container">
&#10;</div>
<div id="comment-tools-65577" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65577-form-container" class="comment-form-container">
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

<span id="65667"></span>

<div id="answer-container-65667" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65667-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65667-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65667-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="novabeat has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>On JOSM, you can also follow another way. First you will have to go to Preference -&gt; Advanced and click on the box at the bottom to activate "Expert" mode.</p>
<p>Then draw two points along the existing way, after that press the "F" key to extend the new way along the old line. Each type you click "F" the new way will extend by one node along the existing way. If you hold down "F", it will keep adding nodes until the way runs out or you come back to the starting node of the way. <a href="https://josm.openstreetmap.de/wiki/Help/Action/FollowLine">https://josm.openstreetmap.de/wiki/Help/Action/FollowLine</a></p>
<p>So if you have an island of reasonable size, and it is completely covered in woodlands with no gaps, you can draw it this way.</p>
<p>But If there is a beach or rocks between the high tide line and the woodland, they you might want to make a different way, at least for those sections where the trees don't meet the water in the aerial imagery. To do this, first make a way along the whole coastline and click to select it. Press "G" to unglue its nodes from the coastline. Then you can press "W" to select "improve way accuracy mode", which will let you move individual nodes away from the coast where there is a beach or rocky area or anything else. You can also hold ctrl to add nodes.</p>
<p>Another way to do this, especially if the coastline is made of more than one way, is to use the Parallel mode. Select a section of coastline or whatever you want to copy, then press shift+P to use Parallel mode. Click and drage the line away from the coast. This works really well for rivers lined with woodland, or to add the water area to a river that is only a line, and so on. You then can use "W" to adjust the new way, for example if there is a beach to gets closer and farther from the water. <a href="https://josm.openstreetmap.de/wiki/Help/Action/Parallel">https://josm.openstreetmap.de/wiki/Help/Action/Parallel</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Sep '18, 08:26</strong></p>
<img src="https://secure.gravatar.com/avatar/984eadc21cb77cb316db4ff21c94b869?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joseph%20E&#39;s gravatar image" />
<p><span>Joseph E</span><br />
<span class="score" title="390 reputation points">390</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joseph E has 2 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-65667" class="comments-container">
&#10;</div>
<div id="comment-tools-65667" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65667-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65578"></span>

<div id="answer-container-65578" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65578-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65578-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65578-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no simply way in josm. Just draw a polygon surrounding all the wooded area and add natural=wood tag.<br />
If some of the polygons of wooded areas also have lakes inside you will probably prefer to map those as a multipolygon relation withe the tag for the wood on the relation and the inner polygon of the water tagged as natural=water. The easy way to do that is draw the outer and inner polygons, select them, then choose ‘create multipolygon’ from one of the menus.<br />
To assist in drawing very large polygons of wooded or water areas there is a ‘fast draw’ plugin that is of great assistance.</p>
<p>Josm info on relations:<br />
<a href="https://learnosm.org/en/josm/josm-relations/">https://learnosm.org/en/josm/josm-relations/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Aug '18, 14:30</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Aug '18, 14:35</strong> </span></p>
</div>
</div>
<div id="comments-container-65578" class="comments-container">
<span id="65585"></span>
<div id="comment-65585" class="comment">
<div id="post-65585-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. This plugin looks promising...</p>
</div>
<div id="comment-65585-info" class="comment-info">
<span class="comment-age">(27 Aug '18, 18:51)</span> <span class="comment-user userinfo">novabeat</span>
</div>
</div>
<span id="65595"></span>
<div id="comment-65595" class="comment">
<div id="post-65595-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If it produces too many nodes you can use the ‘simplify’ function to reduce<br />
<a href="https://josm.openstreetmap.de/wiki/Help/Action/SimplifyWay">https://josm.openstreetmap.de/wiki/Help/Action/SimplifyWay</a></p>
</div>
<div id="comment-65595-info" class="comment-info">
<span class="comment-age">(27 Aug '18, 23:11)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
</div>
<div id="comment-tools-65578" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65578-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65579"></span>

<div id="answer-container-65579" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65579-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(I'm guessing here that the thing that would cause you to "go crazy" is following the coastline, so...)</p>
<p>Just to throw yet another editor into the mix, if you want to have a "forest" polygon follow a section of coastline for a section, in Potlatch2 it's easy - just start drawing the forest along the coast and "f" will follow the other way for as long as you want. Whenever you want to stop following, just continue inland with the forest.</p>
<p>As an example, I've just drawn <a href="https://www.openstreetmap.org/way/620313672">this</a> like that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Aug '18, 14:34</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Aug '18, 14:36</strong> </span></p>
</div>
</div>
<div id="comments-container-65579" class="comments-container">
<span id="65586"></span>
<div id="comment-65586" class="comment">
<div id="post-65586-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. But I can't get Flash to work on my machine... :D</p>
</div>
<div id="comment-65586-info" class="comment-info">
<span class="comment-age">(27 Aug '18, 18:53)</span> <span class="comment-user userinfo">novabeat</span>
</div>
</div>
<span id="65669"></span>
<div id="comment-65669" class="comment">
<div id="post-65669-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>'F' works in JOSM too.</p>
</div>
<div id="comment-65669-info" class="comment-info">
<span class="comment-age">(01 Sep '18, 11:27)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="65679"></span>
<div id="comment-65679" class="comment">
<div id="post-65679-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I used Potlatch 2 and Flash with Google Chrome. see <a href="https://help.openstreetmap.org/questions/48990/potlatch2-not-loading-flash-problem">https://help.openstreetmap.org/questions/48990/potlatch2-not-loading-flash-problem</a></p>
</div>
<div id="comment-65679-info" class="comment-info">
<span class="comment-age">(01 Sep '18, 20:53)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-65579" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65579-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86401"></span>

<div id="answer-container-86401" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86401-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86401-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86401-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm a Newbie too, so take my answer at your own risk: It seems that you can duplicate an area in the iD editor by choosing to create a new area, click on one node of an existing area, then click on the next node of the existing area, then press "F" repeatedly to add subsequent nodes to your new area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '22, 21:48</strong></p>
<img src="https://secure.gravatar.com/avatar/ddc70013a7a45abbaade14957627592c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="M%20Demjanenko&#39;s gravatar image" />
<p><span>M Demjanenko</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="M Demjanenko has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Dec '22, 21:49</strong> </span></p>
</div>
</div>
<div id="comments-container-86401" class="comments-container">
&#10;</div>
<div id="comment-tools-86401" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86401-form-container" class="comment-form-container">
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

