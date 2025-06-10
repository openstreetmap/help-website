+++
type = "question"
title = "Get member by ref tag"
description = '''Hi, I am using the Overpass API / Overpass Turbo to get a single relation (like http://overpass-turbo.eu/s/zog). Here I get the the relation including its members which are some nodes (these are the train stops), ways and some other relations: {&quot;elements&quot;: [  { &quot;type&quot;: &quot;relation&quot;,  &quot;id&quot;: 7796142,  &quot;...'''
date = "2018-06-07T07:30:00Z"
lastmod = "2018-06-07T14:32:00Z"
weight = 64072
keywords = [ "member", "overpass", "reference" ]
aliases = [ "/questions/64072" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Get member by ref tag](/questions/64072/get-member-by-ref-tag)

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
<span id="post-64072-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64072-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64072-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am using the Overpass API / Overpass Turbo to get a single relation (like <a href="http://overpass-turbo.eu/s/zog">http://overpass-turbo.eu/s/zog</a>). Here I get the the relation including its members which are some nodes (these are the train stops), ways and some other relations:</p>
<pre><code>{&quot;elements&quot;: [
   { &quot;type&quot;: &quot;relation&quot;,
     &quot;id&quot;: 7796142,
     &quot;members&quot;: [
      { &quot;type&quot;: &quot;node&quot;,
        &quot;ref&quot;: 2813070487,
        &quot;role&quot;: &quot;stop&quot;
      },
      { &quot;type&quot;: &quot;way&quot;,
        &quot;ref&quot;: 202719939,
        &quot;role&quot;: &quot;platform&quot;
      },
      { &quot;type&quot;: &quot;node&quot;,
        &quot;ref&quot;: 604676237,
        &quot;role&quot;: &quot;stop&quot;
      }, ... ],
}</code></pre>
<p>For a java program I would like to first take the information from one of the ways. Then, in an other API request, ask for the information of its node members. But how can I find the members of a way by only having the information about its "type", "ref", and "role"? I guess I need something like the ID.</p>
<p>I could use the "recursive down" function "&gt;;" to get the nodes but doing so, I loose information about the sorting in which the nodes appear inside the way. In total I want to keep track of the sorting of the whole relation to create a elevation model (that is depending on the geographic coordinates of each node) later on.</p>
<p>My current Overpass query is sorting the nodes and ways by its "role" tag, but how to sort these is another question.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-member" rel="tag" title="see questions tagged &#39;member&#39;">member</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-reference" rel="tag" title="see questions tagged &#39;reference&#39;">reference</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jun '18, 07:30</strong></p>
<img src="https://secure.gravatar.com/avatar/631b4d7ba4195915db6a5b71176b5cee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tigerclaw1993&#39;s gravatar image" />
<p><span>Tigerclaw1993</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tigerclaw1993 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jun '18, 11:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span></p>
</div>
</div>
<div id="comments-container-64072" class="comments-container">
&#10;</div>
<div id="comment-tools-64072" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64072-form-container" class="comment-form-container">
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

<span id="64076"></span>

<div id="answer-container-64076" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64076-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Tigerclaw1993 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The values given for ref <em>are</em> ids.</p>
<p>Each way gives the order of the nodes, so you should be able to use <code>&gt;</code> to get what you want, you'd just need to retrieve the objects of interest from the data returned. The objects aren't in the order you want, <a href="http://overpass-turbo.eu/s/zqe">but the information necessary to construct the order is returned</a>.</p>
<p>The options for sorting the Overpass-API results are limited, <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Print_.28out.29">either by id or using a geographic index</a>. But trying to get results from Overpass-API in a significant order is probably an anti-pattern, better to just retrieve all the necessary data and do the ordering on the client.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '18, 12:09</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-64076" class="comments-container">
<span id="64078"></span>
<div id="comment-64078" class="comment">
<div id="post-64078-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot :)</p>
</div>
<div id="comment-64078-info" class="comment-info">
<span class="comment-age">(07 Jun '18, 14:32)</span> <span class="comment-user userinfo">Tigerclaw1993</span>
</div>
</div>
</div>
<div id="comment-tools-64076" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64076-form-container" class="comment-form-container">
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

