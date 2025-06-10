+++
type = "question"
title = "Is my mapping order for The State of Kuwait areas correct?"
description = '''Hi there, I am trying to map areas in the State of Kuwait. I have started in my area, but I had to stop to get some, best tagging methods. This is how I see the State of Kuwait, admin_level, being played out. Please help if you see a problem.  Kuwait (admin_level=2) Governorates (admin_level=4) we h...'''
date = "2014-04-01T23:34:00Z"
lastmod = "2014-04-04T14:12:00Z"
weight = 32055
keywords = [ "admin_level", "boundary", "relation" ]
aliases = [ "/questions/32055" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is my mapping order for The State of Kuwait areas correct?](/questions/32055/is-my-mapping-order-for-the-state-of-kuwait-areas-correct)

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
<span id="post-32055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32055-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-32055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>I am trying to map areas in the State of Kuwait. I have started in my area, but I had to stop to get some, best tagging methods.</p>
<p>This is how I see the State of Kuwait, admin_level, being played out. Please help if you see a problem.</p>
<ul>
<li>Kuwait (admin_level=2)</li>
<li>Governorates (admin_level=4) we have 6 of them</li>
<li>City (admin_level=7) The capital of the country, and may be 3 others.This is a blurry item.</li>
<li>Suburb (admin_level=8) most of the country seems to fall under this heading. Each suburb has its own mayor of sorts.</li>
<li>Neighbourhood (admin_level=9) Every suburb is broken down into Blocks (neighbourhood) and each Block has streets numbered from 1 up words, ie "Street 1", "Street 2", so forth.</li>
</ul>
<p>This is how address are in Kuwait:<br />
</p>
<pre><code>    City or suburb name, Block number, street number.</code></pre>
<p>Examples:</p>
<pre><code>    Jabriya, Block 8, Street 6, House 24
    Jabriya, Block 7, Street 6, House 24 </code></pre>
These two houses are in the same suburb but different Blocks.
<p>My dilemma is that I am using Boundary Relation to map each Block, and then another boundary relation for the suburb using "boundary=suburb".</p>
<p>What "boundary=*" should I use for the Block or neighbourhood? And should I assign an admin_level to the Block?</p>
<p>I get a warning when in the relation I have "type=boundary" and no "boundary=*"</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-admin_level" rel="tag" title="see questions tagged &#39;admin_level&#39;">admin_level</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '14, 23:34</strong></p>
<img src="https://secure.gravatar.com/avatar/c6b732bd899e8d4b81b7fb16b8066ae9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mohammad%20Asiri&#39;s gravatar image" />
<p><span>Mohammad Asiri</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mohammad Asiri has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-32055" class="comments-container">
&#10;</div>
<div id="comment-tools-32055" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32055-form-container" class="comment-form-container">
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

<span id="32130"></span>

<div id="answer-container-32130" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32130-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32130-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32130-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am a bit confused about OSM objects in Kuwait dealing with boundary=*</p>
<p>Because when going to the well-known webservice <a href="http://overpass-turbo.eu"></a><a href="http://overpass-turbo.eu">http://overpass-turbo.eu</a> , zooming to Kuwait, using the wizard feature of that webpage, and entering there <strong>boundary=</strong>* I only get very few objects.</p>
<p>Is this correct, or dou you have already mapped all the administrative structure of Kuwait in the OSM data? If yes: how did you do that in detail? via border lines and boundary relations?</p>
<p>After getting clear about the relation structure, we can go on to find a solution for your concrete problem, I think.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '14, 14:12</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-32130" class="comments-container">
&#10;</div>
<div id="comment-tools-32130" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32130-form-container" class="comment-form-container">
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

