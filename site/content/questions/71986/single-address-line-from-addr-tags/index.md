+++
type = "question"
title = "Single address line from addr:* tags"
description = '''I would like to show OSM POIs like shops on a map, and display their tag details when clicking on a POI. I would like to remove the addr:* address tags from the details, and instead display them as “full address” on one line. This would turn e.g. addr:street 5th Avenue addr:housenumber 390 addr:unit...'''
date = "2019-12-04T09:35:00Z"
lastmod = "2019-12-07T08:46:00Z"
weight = 71986
keywords = [ "addressing", "poi", "addr", "address" ]
aliases = [ "/questions/71986" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Single address line from addr:\* tags](/questions/71986/single-address-line-from-addr-tags)

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
<span id="post-71986-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71986-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71986-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to show OSM POIs like shops on a map, and display their tag details when clicking on a POI. I would like to remove the addr:* address tags from the details, and instead display them as “full address” on one line.</p>
<p>This would turn e.g.</p>
<pre><code>addr:street       5th Avenue
addr:housenumber  390
addr:unit         411
addr:city         New York
addr:postcode     10018
addr:state        NY</code></pre>
<p>into</p>
<pre><code>390, 5th Avenue, Unit 411, New York, NY, 10018</code></pre>
<p>I’m fully aware that</p>
<p>a) Addressing systems around the world are different and complicated: Some places use blocks or suburbs instead of streets, you need unit or apartment numbers, addresses can be multilingual, and so on.<br />
b) Conventions how to order address parts differ locally, e.g. putting the housenumber before or after the street, or putting the postcode before or after the city.<br />
c) Address information in OSM can be incomplete, addresses for POIs would need to be taken from a surrounding building, etc.</p>
<p>Is there some description of rules how to put the address parts together? Maybe different rules per region?</p>
<p>Alternatively, is there a universal rule that could be applied and results in addresses that are mostly understood worldwide? Something like “Use addr:* in this order: housenumber, street, block, …; omit any missing tag; comma-separate them”</p>
<p>Is there even some code or library which implements something like this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-addressing" rel="tag" title="see questions tagged &#39;addressing&#39;">addressing</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span> <span class="post-tag tag-link-addr" rel="tag" title="see questions tagged &#39;addr&#39;">addr</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Dec '19, 09:35</strong></p>
<img src="https://secure.gravatar.com/avatar/97f754e0356a74acc666550948b48bd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hfs&#39;s gravatar image" />
<p><span>hfs</span><br />
<span class="score" title="851 reputation points">851</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hfs has 3 accepted answers">17%</span> </br></br></p>
</div>
</div>
<div id="comments-container-71986" class="comments-container">
&#10;</div>
<div id="comment-tools-71986" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71986-form-container" class="comment-form-container">
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

<span id="72028"></span>

<div id="answer-container-72028" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72028-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72028-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72028-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hfs has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at <a href="https://github.com/OpenCageData/address-formatting">the address format project from OpenCageData</a>. This is a project that collects the different formats for all countries around the world and also provides scripts for formatting.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '19, 08:46</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-72028" class="comments-container">
&#10;</div>
<div id="comment-tools-72028" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72028-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71989"></span>

<div id="answer-container-71989" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71989-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are so many different address formats. See (for example) <a href="https://www.grcdi.nl/gsb/world%20address%20formats.html">this site</a>. I am not aware of an existing OSM tool to format an address based on country, although that doesn't mean there isn't one.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Dec '19, 11:28</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-71989" class="comments-container">
<span id="71990"></span>
<div id="comment-71990" class="comment">
<div id="post-71990-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That site is wrong, there are villages in the UK, Switzerland and France where the roads do not have names (there may be quarters/viertel or hamlets with names which may be useful for addressing. Specific examples Scuol, Ftan, Ardez in the Engadin, Plounevezel in Finistere. Additionally, in some villages in the UK, there may be street names but these are not conventionally part of the address (e.g., Caio).</p>
</div>
<div id="comment-71990-info" class="comment-info">
<span class="comment-age">(04 Dec '19, 11:39)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="71991"></span>
<div id="comment-71991" class="comment">
<div id="post-71991-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I was using it more to illustrate there are lots of formats rather than it being an exhaustive list. I've just checked a postcode from a house in a local hamlet on an unnamed road, and the Postcode Finder on the Royal Mail website has them as house name, hamlet name, parish name, postal town, postcode.</p>
</div>
<div id="comment-71991-info" class="comment-info">
<span class="comment-age">(04 Dec '19, 12:00)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71989" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71989-form-container" class="comment-form-container">
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

