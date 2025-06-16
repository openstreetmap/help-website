+++
type = "question"
title = "Addresses with two house numbers?"
description = '''In the US, we have a lot of address that have two house numbers associated with them: a house number and an apartment/unit/lot/suite number. The number on the front door is always the more specific apartment/unit/lot/suite number, though sometimes the more general street house number is included as ...'''
date = "2011-01-20T19:26:00Z"
lastmod = "2015-06-16T17:48:00Z"
weight = 2329
keywords = [ "addressing", "housenumbers" ]
aliases = [ "/questions/2329" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Addresses with two house numbers?](/questions/2329/addresses-with-two-house-numbers)

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
<span id="post-2329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2329-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In the US, we have a lot of address that have two house numbers associated with them: a house number and an apartment/unit/lot/suite number. The number on the front door is always the more specific apartment/unit/lot/suite number, though sometimes the more general street house number is included as well.</p>
<p>For manufactured homes in a mobile home park, there is often one house number for the whole area and then each house gets a lot number. For example, the street address of a house might be:</p>
<p>25 Maple Street Lot 7</p>
<p>More likely than not, the number 25 will not be on the house at all, but only the number 7. So that would lead me to believe that we can use a way with building=yes, addr:housenumber=7 and addr:street=Maple Street, but the street address 7 Maple Street would be somewhere else entirely, so it seems like the 25 part of the address needs to be captured some way. Alternatively, you could tag every house in the subdivision with addr:housenumber=25, but then you could differentiate the houses from each other.</p>
<p>Another example is townhouses where you have things like</p>
<p>25 Maple Street Unit 3</p>
<p>In this case, you probably don't have separate buildings, so you can put building=yes, addr:housenumber=25 and addr:street=Maple Street on the way for the building, and you can put addr:housenumber=3 on the node for the entrance to unit 3, but again how do you avoid confusion with the house at 3 Maple Street?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-addressing" rel="tag" title="see questions tagged &#39;addressing&#39;">addressing</span> <span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jan '11, 19:26</strong></p>
<img src="https://secure.gravatar.com/avatar/22748312961cdceb5419decc3cc5faad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter%20Dobratz&#39;s gravatar image" />
<p><span>Peter Dobratz</span><br />
<span class="score" title="311 reputation points">311</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter Dobratz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jan '11, 23:00</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-2329" class="comments-container">
&#10;</div>
<div id="comment-tools-2329" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2329-form-container" class="comment-form-container">
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

<span id="43589"></span>

<div id="answer-container-43589" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43589-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-43589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The general consensus on <a href="https://wiki.openstreetmap.org/wiki/Key:addr">addr:* tags</a> now seems to be to put the main number in addr:housenumber and the minor number in addr:unit. In the example above for 25 Maple St Unit 3, we would have the following:</p>
<pre><code>addr:housenumber=25
addr:street=Maple Street
addr:unit=3</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jun '15, 17:48</strong></p>
<img src="https://secure.gravatar.com/avatar/22748312961cdceb5419decc3cc5faad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter%20Dobratz&#39;s gravatar image" />
<p><span>Peter Dobratz</span><br />
<span class="score" title="311 reputation points">311</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter Dobratz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43589" class="comments-container">
&#10;</div>
<div id="comment-tools-43589" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43589-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2335"></span>

<div id="answer-container-2335" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2335-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-2335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What I do where a building contains multiple apartments is to tag it with addr:housenumber or addr:housename to indicate the address of the block, and then add addr:flatnumber to indicate which apartment numbers exist in the building. So you would have something like:</p>
<pre><code>addr:street=Foo Street
addr:housenumber=25
addr:flatnumber=1-6</code></pre>
<p>or, if the block is named:</p>
<pre><code>addr:street=Bar Street
addr:housename=Baz House
addr:flatnumber=1-25</code></pre>
<p>I think the wiki also has a tag for specifying how to interpolate the flat numbers if the block only contains odd or even numbers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jan '11, 23:03</strong></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomH has 9 accepted answers">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jan '11, 23:03</strong> </span></p>
</div>
</div>
<div id="comments-container-2335" class="comments-container">
<span id="2345"></span>
<div id="comment-2345" class="comment">
<div id="post-2345-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'll add the links in my answer instead. Too hard to use these fields..</p>
</div>
<div id="comment-2345-info" class="comment-info">
<span class="comment-age">(21 Jan '11, 09:10)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
</div>
<div id="comment-tools-2335" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2335-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2332"></span>

<div id="answer-container-2332" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2332-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There seems to be many ways to do this in the wild, while searching I've seen:</p>
<ul>
<li><a href="http://www.google.se/search?q=building%3Dentrance+ref+openstreetmap.org+inurl:browse+site:openstreetmap.org">building=entrance + ref=*</a> more than 20 usages around the world, means flat "D" (can't do a search for that</li>
<li><a href="http://taginfo.openstreetmap.de/keys/addr:flatnumber#values">addr:flatnumber</a> 50 usages in world, + addr:flatnumber:interpolation=all/even/odd (just used once)</li>
</ul>
<p>But I still think this is a general problem, there exist many places that have only one housenumber or address but include many sub addresses.</p>
<ul>
<li>Unit numbers</li>
<li>Entrance numbers</li>
<li>Building numbers</li>
<li>Tent location</li>
<li>Parking numbers</li>
<li>Cabin numbers (in hotels)</li>
</ul>
<p>Perhaps something like:</p>
<pre><code>addr:subnumber=* 
title:addr:subnumber=Lot</code></pre>
<p>or</p>
<pre><code>ref=b-k
ref:title=flat/lot/entrance/blabla?</code></pre>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jan '11, 21:44</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jan '11, 09:28</strong> </span></p>
</div>
</div>
<div id="comments-container-2332" class="comments-container">
&#10;</div>
<div id="comment-tools-2332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2332-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2331"></span>

<div id="answer-container-2331" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2331-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-2331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Can't you use something like <code>addr:housenumber=25/7</code> for 25 Maple Street Lot 7? The housenumber tag allows alphanumeric characters not just numbers. So you could even write something like <code>addr:housenumber=25 Lot 7</code>. I think this solves your problem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jan '11, 20:57</strong></p>
<img src="https://secure.gravatar.com/avatar/3f398da25e1453020723c955139a4ec7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ALE&#39;s gravatar image" />
<p><span>ALE</span><br />
<span class="score" title="1943 reputation points"><span>1.9k</span></span><span title="41 badges"><span class="badge1">●</span><span class="badgecount">41</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ALE has 4 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-2331" class="comments-container">
<span id="2333"></span>
<div id="comment-2333" class="comment">
<div id="post-2333-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would probably do a separate node for "addr:housenumber=25" and then add tag the lots with addr:housenumber=Lot 7; addr:street=Maplestreet 25</p>
</div>
<div id="comment-2333-info" class="comment-info">
<span class="comment-age">(20 Jan '11, 21:45)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
<span id="2348"></span>
<div id="comment-2348" class="comment">
<div id="post-2348-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I think you should not put the number in the addr:street tag because this will cause problems for navigation programs. The might not find the address and / or housenumber.</p>
</div>
<div id="comment-2348-info" class="comment-info">
<span class="comment-age">(21 Jan '11, 11:06)</span> <span class="comment-user userinfo">ALE</span>
</div>
</div>
<span id="2360"></span>
<div id="comment-2360" class="comment">
<div id="post-2360-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>makes sense.</p>
</div>
<div id="comment-2360-info" class="comment-info">
<span class="comment-age">(22 Jan '11, 09:22)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
</div>
<div id="comment-tools-2331" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2331-form-container" class="comment-form-container">
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

