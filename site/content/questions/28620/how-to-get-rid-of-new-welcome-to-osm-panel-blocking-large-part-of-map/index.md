+++
type = "question"
title = "How to get rid of new &quot;Welcome to OSM&quot; panel blocking large part of map?"
description = '''Today when I went to browse OSM, I noticed new controls on the map. Great, looks good. But, there&#x27;s a massive &quot;Welcome to OSM&quot; panel blocking a large portion of the top-left of the map, and I can&#x27;t find any way to get rid of it. Can anybody tell me how to close it? Thanks a lot.'''
date = "2013-11-30T17:38:00Z"
lastmod = "2020-06-19T09:17:00Z"
weight = 28620
keywords = [ "osm.org", "map", "controls" ]
aliases = [ "/questions/28620" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [How to get rid of new "Welcome to OSM" panel blocking large part of map?](/questions/28620/how-to-get-rid-of-new-welcome-to-osm-panel-blocking-large-part-of-map)

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
<span id="post-28620-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28620-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-28620-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Today when I went to browse OSM, I noticed new controls on the map. Great, looks good. But, there's a massive "Welcome to OSM" panel blocking a large portion of the top-left of the map, and I can't find any way to get rid of it. Can anybody tell me how to close it? Thanks a lot.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm.org" rel="tag" title="see questions tagged &#39;osm.org&#39;">osm.org</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-controls" rel="tag" title="see questions tagged &#39;controls&#39;">controls</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '13, 17:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a8992ad9a83eacdd6388ed265d3f6921?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tongro&#39;s gravatar image" />
<p><span>tongro</span><br />
<span class="score" title="701 reputation points">701</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tongro has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Dec '13, 02:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-28620" class="comments-container">
&#10;</div>
<div id="comment-tools-28620" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28620-form-container" class="comment-form-container">
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

<span id="28621"></span>

<div id="answer-container-28621" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28621-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-28621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tongro has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's now an [X] button with which to close the message. It also goes away by itself when you log in. If neither of these work for you, consider a GreaseMonkey script like this:</p>
<pre><code>// ==UserScript==
// @name     Remove OSM welcome box
// @include  https://www.openstreetmap.org/*
// ==/UserScript==
&#10;var welcome = $(&quot;div.welcome&quot;);
if (welcome) welcome.remove ();</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '13, 17:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Dec '13, 11:44</strong> </span></p>
</div>
</div>
<div id="comments-container-28621" class="comments-container">
<span id="28694"></span>
<div id="comment-28694" class="comment">
<div id="post-28694-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Great! It works! Good job! Thanks!</p>
</div>
<div id="comment-28694-info" class="comment-info">
<span class="comment-age">(02 Dec '13, 15:11)</span> <span class="comment-user userinfo">hubeat</span>
</div>
</div>
<span id="28732"></span>
<div id="comment-28732" class="comment">
<div id="post-28732-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmm, it doesn't work for me so far. I installed a random script in order to get an editable new script, filled in that code, but the small box is still there. Any suggestions, as to how it would work better?</p>
</div>
<div id="comment-28732-info" class="comment-info">
<span class="comment-age">(03 Dec '13, 17:48)</span> <span class="comment-user userinfo">abr01</span>
</div>
</div>
<span id="28733"></span>
<div id="comment-28733" class="comment">
<div id="post-28733-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Never mind the script - you do know that there is an [X] button with which to close the message now, don't you? Maybe a screenshot would help?</p>
</div>
<div id="comment-28733-info" class="comment-info">
<span class="comment-age">(03 Dec '13, 17:49)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="28735"></span>
<div id="comment-28735" class="comment not_top_scorer">
<div id="post-28735-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't see any [x] button here, sorry. Maybe, because i stay logged in, having only the smaller box visible?</p>
</div>
<div id="comment-28735-info" class="comment-info">
<span class="comment-age">(03 Dec '13, 18:42)</span> <span class="comment-user userinfo">abr01</span>
</div>
</div>
<span id="28736"></span>
<div id="comment-28736" class="comment not_top_scorer">
<div id="post-28736-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So it's the search box, not the welcome box, that you'd like to remove, is it? Or would you like to move it somewhere else?</p>
</div>
<div id="comment-28736-info" class="comment-info">
<span class="comment-age">(03 Dec '13, 18:46)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="28738"></span>
<div id="comment-28738" class="comment">
<div id="post-28738-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, it's the search box then. I would like to have all real estate for the map, no intrusive boxes at all, if possible. Thanks.</p>
</div>
<div id="comment-28738-info" class="comment-info">
<span class="comment-age">(03 Dec '13, 19:46)</span> <span class="comment-user userinfo">abr01</span>
</div>
</div>
<span id="28740"></span>
<div id="comment-28740" class="comment">
<div id="post-28740-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Consider using an alternative site such as <a href="http://www.informationfreeway.org/">http://www.informationfreeway.org/</a> or <a href="http://opencyclemap.org/,">http://opencyclemap.org/,</a> both of which offer views on OSM data without the community information around it. osm.org itself is not principally a map-viewing site.</p>
</div>
<div id="comment-28740-info" class="comment-info">
<span class="comment-age">(03 Dec '13, 20:13)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="28747"></span>
<div id="comment-28747" class="comment not_top_scorer">
<div id="post-28747-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When i first discovered OSM in 2005 i wanted a map. I then read and learnt about the project and liked the idea. I started to record GPX traces and eventually edit the map. I think the map should be the first view we see otherwise new possible contributors may click away when the don't see a map or a map button.</p>
</div>
<div id="comment-28747-info" class="comment-info">
<span class="comment-age">(03 Dec '13, 23:09)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="28774"></span>
<div id="comment-28774" class="comment not_top_scorer">
<div id="post-28774-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Richard</span>: thanks, i've tested informationfreeway, but i'll stick to OpenStreetMap, because the other one doesn't offer to navigate via arrow keys / zoom in/out.</p>
</div>
<div id="comment-28774-info" class="comment-info">
<span class="comment-age">(04 Dec '13, 13:41)</span> <span class="comment-user userinfo">abr01</span>
</div>
</div>
</div>
<div id="comment-tools-28621" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-28621-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75377"></span>

<div id="answer-container-75377" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75377-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The [X] is almost completely hidden by the text of "OpenStreetMap!"</p>
<p><img src="https://live.staticflickr.com/65535/50021966876_189e3ac50c_o_d.png" alt="invisible x" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '20, 09:17</strong></p>
<img src="https://secure.gravatar.com/avatar/f2410b4e8fcb9b559851ecf1b256a1ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hackery&#39;s gravatar image" />
<p><span>hackery</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hackery has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jun '20, 09:35</strong> </span></p>
</div>
</div>
<div id="comments-container-75377" class="comments-container">
&#10;</div>
<div id="comment-tools-75377" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75377-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28775"></span>

<div id="answer-container-28775" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28775-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What happened to my answer i've just posted?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Dec '13, 13:46</strong></p>
<img src="https://secure.gravatar.com/avatar/9fec126cd5166a4cf290b96dfe3df6ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abr01&#39;s gravatar image" />
<p><span>abr01</span><br />
<span class="score" title="66 reputation points">66</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abr01 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28775" class="comments-container">
<span id="28776"></span>
<div id="comment-28776" class="comment">
<div id="post-28776-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>It is there just click show 4 more comments... then delete your "what happened...answer" and my comment will disappear as well</p>
</div>
<div id="comment-28776-info" class="comment-info">
<span class="comment-age">(04 Dec '13, 14:01)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-28775" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28775-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74902"></span>

<div id="answer-container-74902" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74902-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The X is tiny and in a shade that makes it very difficult to see. I had to zoom the view a lot before I found it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 May '20, 13:42</strong></p>
<img src="https://secure.gravatar.com/avatar/d057df81a308f4c07d62653769847fda?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pmaguire&#39;s gravatar image" />
<p><span>pmaguire</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pmaguire has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74902" class="comments-container">
&#10;</div>
<div id="comment-tools-74902" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74902-form-container" class="comment-form-container">
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

