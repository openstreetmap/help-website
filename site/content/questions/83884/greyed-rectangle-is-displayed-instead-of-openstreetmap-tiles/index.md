+++
type = "question"
title = "Greyed Rectangle is displayed instead of OpenStreetMap tiles"
description = '''I am unable to load OpenStreetMap in Folium on Jupyter Notebook. It&#x27;s just some grey rectangle that displays. Anyone knows what may be causing this? I also tried with Leafmaps and IPyleaflet instead of Folium, but nothing is working. Thanks!'''
date = "2022-03-16T15:26:00Z"
lastmod = "2022-03-16T16:16:00Z"
weight = 83884
keywords = [ "jupyter", "folium" ]
aliases = [ "/questions/83884" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Greyed Rectangle is displayed instead of OpenStreetMap tiles](/questions/83884/greyed-rectangle-is-displayed-instead-of-openstreetmap-tiles)

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
<span id="post-83884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83884-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am unable to load OpenStreetMap in Folium on Jupyter Notebook. It's just some grey rectangle that displays. Anyone knows what may be causing this? I also tried with Leafmaps and IPyleaflet instead of Folium, but nothing is working. Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-jupyter" rel="tag" title="see questions tagged &#39;jupyter&#39;">jupyter</span> <span class="post-tag tag-link-folium" rel="tag" title="see questions tagged &#39;folium&#39;">folium</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Mar '22, 15:26</strong></p>
<img src="https://secure.gravatar.com/avatar/d53d184e0887d9e140a16505cf455237?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gcalix&#39;s gravatar image" />
<p><span>gcalix</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gcalix has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83884" class="comments-container">
&#10;</div>
<div id="comment-tools-83884" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83884-form-container" class="comment-form-container">
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

<span id="83885"></span>

<div id="answer-container-83885" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83885-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-83885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://operations.osmfoundation.org/policies/tiles/">OSM tile usage policy</a> requires: "Valid HTTP User-Agent identifying application. Faking another app’s User-Agent WILL get you blocked." and "DO NOT send no-cache headers. (“Cache-Control: no-cache”, “Pragma: no-cache” etc.)" - is it possible that your setup falls foul of these?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Mar '22, 15:31</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Mar '22, 15:33</strong> </span></p>
</div>
</div>
<div id="comments-container-83885" class="comments-container">
<span id="83886"></span>
<div id="comment-83886" class="comment">
<div id="post-83886-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmmm... I'm not sure what these are. I'm working in Jupyter Notebook. Is there a way to check if these policies are satisfied?</p>
<p>I am able to work and view the OpenStreetMap tiles a day or two ago, but recently started to not work. So I'm not sure what happened.</p>
</div>
<div id="comment-83886-info" class="comment-info">
<span class="comment-age">(16 Mar '22, 15:35)</span> <span class="comment-user userinfo">gcalix</span>
</div>
</div>
<span id="83888"></span>
<div id="comment-83888" class="comment">
<div id="post-83888-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The rule has always been there but the implementation of the rule has <a href="https://lists.openstreetmap.org/pipermail/talk/2022-March/087367.html">changed over the past weekend</a> so maybe that is the issue.</p>
</div>
<div id="comment-83888-info" class="comment-info">
<span class="comment-age">(16 Mar '22, 15:45)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="83889"></span>
<div id="comment-83889" class="comment">
<div id="post-83889-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok I see, probably that's what happened. But I'm not sure what to do. How can I fix it so that I can view the OpenStreetMap tiles again?</p>
</div>
<div id="comment-83889-info" class="comment-info">
<span class="comment-age">(16 Mar '22, 15:50)</span> <span class="comment-user userinfo">gcalix</span>
</div>
</div>
<span id="83891"></span>
<div id="comment-83891" class="comment">
<div id="post-83891-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Edit: I'm currently working on Jupyter Notebook, but I just tested on Google Colab and it seemed to work fine. Then I tried it on Jupyter Notebook on a different browser (Safari) and it works ok. So it seems like the browser that I am currently working on has some problems communicating with Jupyter (currently using Brave). So pretty sure the problem here is Brave.</p>
</div>
<div id="comment-83891-info" class="comment-info">
<span class="comment-age">(16 Mar '22, 16:16)</span> <span class="comment-user userinfo">gcalix</span>
</div>
</div>
</div>
<div id="comment-tools-83885" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83885-form-container" class="comment-form-container">
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

