+++
type = "question"
title = "How to tag slums, shanty towns, favelas, villas miseria?"
description = '''I was having a look at the &quot;proyecto mapear&quot; in Argentina and they offer free maps (means &quot;no cost maps&quot; here) for Garmin GPS navigation devices which include also the display of what they call &quot;zonas peligros&quot; (dangerous zones). Those &quot;zonas peligros&quot; are villas miserias (slums, shanty towns) which...'''
date = "2011-02-22T14:04:00Z"
lastmod = "2011-02-23T13:13:00Z"
weight = 3270
keywords = [ "slum", "favela", "tagging", "villa_miseria", "shanty_town" ]
aliases = [ "/questions/3270" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag slums, shanty towns, favelas, villas miseria?](/questions/3270/how-to-tag-slums-shanty-towns-favelas-villas-miseria)

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
<span id="post-3270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3270-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-3270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was having a look at the <a href="http://www.proyectomapear.com.ar/">"proyecto mapear"</a> in Argentina and they offer free maps (means "no cost maps" here) for Garmin GPS navigation devices which include also the display of what they call "zonas peligros" (dangerous zones). Those "zonas peligros" are villas miserias (slums, shanty towns) which are not safe to pass by car or on foot.</p>
<p>I was wondering whether OSM also has a tagging scheme for such shanty towns (e.g. Kibera in Nigeria, Villa 31 in Argentina, etc.). How do you tag such zones?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-slum" rel="tag" title="see questions tagged &#39;slum&#39;">slum</span> <span class="post-tag tag-link-favela" rel="tag" title="see questions tagged &#39;favela&#39;">favela</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-villa_miseria" rel="tag" title="see questions tagged &#39;villa_miseria&#39;">villa_miseria</span> <span class="post-tag tag-link-shanty_town" rel="tag" title="see questions tagged &#39;shanty_town&#39;">shanty_town</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Feb '11, 14:04</strong></p>
<img src="https://secure.gravatar.com/avatar/3f398da25e1453020723c955139a4ec7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ALE&#39;s gravatar image" />
<p><span>ALE</span><br />
<span class="score" title="1943 reputation points"><span>1.9k</span></span><span title="41 badges"><span class="badge1">●</span><span class="badgecount">41</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ALE has 4 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Feb '11, 16:30</strong> </span></p>
</div>
</div>
<div id="comments-container-3270" class="comments-container">
&#10;</div>
<div id="comment-tools-3270" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3270-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="3298"></span>

<div id="answer-container-3298" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3298-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-3298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ALE has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Map it! Rendering and use is another problem, keep a top tag that is documented as subjective and then let people find other tags that are hard facts.</p>
<p>The problem isn't really about whether a part of the town is a slum or not it's about limiting the scope of the tag. You want to tag areas that might be dangerous, these areas are pretty easy to find if you talk with local people so map recommendations.</p>
<p>The meaning of the recommendation "don't go there if you are a tourist" is different in São Paulo, Baghdad or Cuzco. But that doesn't mean you actually have to care about the differences, just map it as a subjective danger_zone and let people who want to use it find better tags to specify it.</p>
<p>As for the tag name?</p>
<ul>
<li>recommendation=no_go_zone</li>
<li>danger=violence</li>
<li>crimes:high=2005</li>
<li>police_protection=low</li>
<li>danger:for:gringos=high</li>
<li>unsafe_for=turist</li>
<li>boundary=unsafe_zone</li>
<li>cocaine_selling=yes</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Feb '11, 08:54</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-3298" class="comments-container">
<span id="3306"></span>
<div id="comment-3306" class="comment">
<div id="post-3306-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I specifically like the tag "danger:for:gringos=high" ;-) . But are some of the tags mentioned above already in use? Were there already discussions about this issue?</p>
</div>
<div id="comment-3306-info" class="comment-info">
<span class="comment-age">(23 Feb '11, 11:56)</span> <span class="comment-user userinfo">ALE</span>
</div>
</div>
<span id="3308"></span>
<div id="comment-3308" class="comment">
<div id="post-3308-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have seen no such discussion.</p>
</div>
<div id="comment-3308-info" class="comment-info">
<span class="comment-age">(23 Feb '11, 13:13)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
</div>
<div id="comment-tools-3298" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3298-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3271"></span>

<div id="answer-container-3271" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3271-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3271-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-3271-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The short answer is: One man's slum is another man's <a href="http://wiki.openstreetmap.org/wiki/Tag:landuse%3Dresidential">landuse=residential</a></p>
<p>"dangerous zones" is rather subjective. I guess cities in Argentina are similar to São Paulo which I have visited a few times. The favelas mostly stick out with surprising contrast against more wealthy residential areas, so in these cases it would be quite easy to make a judgement about which area is slum and which isn't, but that's a slippery slope towards all kinds of debates which we try to avoid by only mapping things (and inventing tagging schemes) which are "verifiable". We avoid subjective judgements and fuzzy scales. See <a href="http://wiki.openstreetmap.org/wiki/Verifiability">Verifiability</a></p>
<p>You could devise a separate mapping project built on top of OpenStreetMap, to gather this kind of data. For example there are a lot of initiatives set up to do "crime mapping"</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Feb '11, 14:21</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-3271" class="comments-container">
<span id="3272"></span>
<div id="comment-3272" class="comment">
<div id="post-3272-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You are right. It is subjective to some extend. However I think it could be important for routing. I remember some Germans getting shot in Miami because they took the wrong exit from the interstate.</p>
</div>
<div id="comment-3272-info" class="comment-info">
<span class="comment-age">(22 Feb '11, 14:35)</span> <span class="comment-user userinfo">ALE</span>
</div>
</div>
</div>
<div id="comment-tools-3271" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3271-form-container" class="comment-form-container">
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

