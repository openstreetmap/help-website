+++
type = "question"
title = "How to isolate the 2 lists of ways for each driving direction in a Motorway relation ?"
description = '''Hello, I&#x27;m interested in the way &quot;Motorways&quot; are described in OSM. For instance that one : http://www.openstreetmap.org/browse/relation/107088 describes a motorway between 2 cities : Paris and Lille (North of France). However the members of the relation are for both driving directions : Paris -&amp;gt; ...'''
date = "2011-02-19T20:35:00Z"
lastmod = "2011-03-01T11:32:00Z"
weight = 3205
keywords = [ "motorway", "relations", "highway" ]
aliases = [ "/questions/3205" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to isolate the 2 lists of ways for each driving direction in a Motorway relation ?](/questions/3205/how-to-isolate-the-2-lists-of-ways-for-each-driving-direction-in-a-motorway-relation)

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
<span id="post-3205-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3205-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3205-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,<br />
I'm interested in the way "Motorways" are described in OSM.<br />
For instance that one :<br />
<a href="http://www.openstreetmap.org/browse/relation/107088">http://www.openstreetmap.org/browse/relation/107088</a><br />
describes a motorway between 2 cities : Paris and Lille (North of France).<br />
However the members of the relation are for both driving directions : Paris -&gt; Lille <strong>AND</strong> Lille-&gt;Paris .<br />
Is there an "easy" way to know which ways are part of the Paris-&gt;Lille driving direction and which ones are only relevant for the other driving direction (=split the relation in two parts, one for each driving direction) ?<br />
Any hint or idea is welcome to extract such information from the relation !<br />
Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-motorway" rel="tag" title="see questions tagged &#39;motorway&#39;">motorway</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Feb '11, 20:35</strong></p>
<img src="https://secure.gravatar.com/avatar/d43d3db062e0ec88d26207ba81878941?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="y0n3l&#39;s gravatar image" />
<p><span>y0n3l</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="y0n3l has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Feb '11, 20:43</strong> </span></p>
</div>
</div>
<div id="comments-container-3205" class="comments-container">
&#10;</div>
<div id="comment-tools-3205" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3205-form-container" class="comment-form-container">
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

<span id="3229"></span>

<div id="answer-container-3229" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3229-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-3229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The best solution would be to split the relation into two parts, one for each driving direction. In the US, directional roles have been used: north/south/east/west, but this does not seem to be the convention in France.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '11, 12:40</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span> </br></br></p>
</div>
</div>
<div id="comments-container-3229" class="comments-container">
<span id="3459"></span>
<div id="comment-3459" class="comment">
<div id="post-3459-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would include the two new relations in a super relatin, too</p>
</div>
<div id="comment-3459-info" class="comment-info">
<span class="comment-age">(28 Feb '11, 20:56)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-3229" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3229-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3257"></span>

<div id="answer-container-3257" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3257-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3257-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3257-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not that an easy solution exists. Maybe you can code (for example with python and DOM) an analyser on the data that, starting from a node, build the set of ways that are connected.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Feb '11, 09:26</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span> </br></br></p>
</div>
</div>
<div id="comments-container-3257" class="comments-container">
<span id="3410"></span>
<div id="comment-3410" class="comment">
<div id="post-3410-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello Nicolas, Yes this is what I ended up with : I split the relation in x parts on my side by finding which ways have common nodes.</p>
</div>
<div id="comment-3410-info" class="comment-info">
<span class="comment-age">(27 Feb '11, 14:20)</span> <span class="comment-user userinfo">y0n3l</span>
</div>
</div>
<span id="3438"></span>
<div id="comment-3438" class="comment">
<div id="post-3438-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Good. Maybe you can flag your question as answered :-) And it will be nice to post your script if it is possible.</p>
</div>
<div id="comment-3438-info" class="comment-info">
<span class="comment-age">(28 Feb '11, 10:42)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
<span id="3457"></span>
<div id="comment-3457" class="comment">
<div id="post-3457-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I'll flag the question as answered, but I was waiting for a little while to see different answers (actually I think that Mike's answer is the right one, after a more in depth look , I saw that some french highways were using this tag, but only a few of them). For the scripts , humpf, it's written in ObjectiveC so unless you're in the Mac / iOS I think it's useless :/ Are you the guy from <a href="http://pld.dumoulin63.net">http://pld.dumoulin63.net</a> ? I'm also on open street map fr ;)</p>
</div>
<div id="comment-3457-info" class="comment-info">
<span class="comment-age">(28 Feb '11, 20:31)</span> <span class="comment-user userinfo">y0n3l</span>
</div>
</div>
<span id="3464"></span>
<div id="comment-3464" class="comment">
<div id="post-3464-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, ObjectiveC will be useless for me. Yes, it's the same dumoulin ;-)</p>
</div>
<div id="comment-3464-info" class="comment-info">
<span class="comment-age">(01 Mar '11, 08:43)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
</div>
<div id="comment-tools-3257" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3257-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3470"></span>

<div id="answer-container-3470" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3470-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could try ignoring relations, and extracting "WayChains". A chain of ways that are connected end-to-end.</p>
<p>My <a href="http://wiki.openstreetmap.org/wiki/Waychains_TIGER_fixup">WayChains TIGER fixup</a> analysis does this kind of thing (on motorways as it happens, although it would work for other kinds of end-to-end connected ways)</p>
<p>The logic to join together ways into "waychains" can be found in <a href="http://harrywood.dev.openstreetmap.org/waychains/waychainsummary.rb">waychainsummary.rb</a>.</p>
<p>I'm running it with a pre-processing step using my <a href="http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#--simplify">osmosis simplify plugin</a>, which reduces ways down to just their start node and end node.</p>
<p>Note however that I was deliberately designing this to help find problems in the U.S. motorways data. For extracting OpenStreetMap data for practical use, you may find this approach a little fragile. e.g. if a mapper tags an onramp with highway=motorway instead of highway=motorway_link, then it may not chain the ways correctly at that point. You'd have to fix it before trying again.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '11, 11:32</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span> </br></br></p>
</div>
</div>
<div id="comments-container-3470" class="comments-container">
&#10;</div>
<div id="comment-tools-3470" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3470-form-container" class="comment-form-container">
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

