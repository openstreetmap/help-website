+++
type = "question"
title = "Overpass Turbo: How to find all intersecting roads over AND under a motorway without making 2 separate queries"
description = '''Greetings - I&#x27;m trying to write an Overpass-QL query to find all roads crossing a motorway/freeway - both on bridges above and bridged below. The above-the-road part is easy, but below is proving difficult. Is there syntax to use &#x27;around(0)&#x27; to find something that FOO way is crossing above, but filt...'''
date = "2022-03-01T19:19:00Z"
lastmod = "2022-03-09T19:56:00Z"
weight = 83621
keywords = [ "filter", "crossing", "ways", "overpass-turbo", "overpass-ql" ]
aliases = [ "/questions/83621" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass Turbo: How to find all intersecting roads over AND under a motorway without making 2 separate queries](/questions/83621/overpass-turbo-how-to-find-all-intersecting-roads-over-and-under-a-motorway-without-making-2-separate-queries)

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
<span id="post-83621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83621-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Greetings -</p>
<p>I'm trying to write an Overpass-QL query to find all roads crossing a motorway/freeway - both on bridges above and bridged below. The above-the-road part is easy, but below is proving difficult. Is there syntax to use 'around(0)' to find something that FOO way is crossing above, but filtering out FOO itself? I tried using a ["ref"!~"FOO"] argument to filter it out, but that's not working.<br />
I've been looking at this for too long, and my brain is mush. Help? Someone...?</p>
<p>Here's what I have:</p>
<pre><code>[out:json][timeout:30][bbox:{{bbox}}];
&#10;way[&quot;ref&quot;~&quot;FOO&quot;]-&gt;.road;
way(around.road:0)[bridge][&quot;highway&quot;~&quot;^((primary|secondary|tertiary|trunk|motorway)(_link)?|service|residential|unclassified)&quot;]-&gt;.xbridges;
way.road[bridge]-&gt;.br;
way(around.br:0)[&quot;highway&quot;~&quot;^((primary|secondary|tertiary|trunk|motorway)(_link)?|service|residential|unclassified)&quot;][&quot;ref&quot;!~&quot;FOO&quot;]-&gt;.xways;
(.xways;
 .xbridges;);
out geom;</code></pre>
<p>Thanks so much....</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-crossing" rel="tag" title="see questions tagged &#39;crossing&#39;">crossing</span> <span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Mar '22, 19:19</strong></p>
<img src="https://secure.gravatar.com/avatar/31ab4a3a30ec105540eb6d56c8ad98c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GregRetro&#39;s gravatar image" />
<p><span>GregRetro</span><br />
<span class="score" title="354 reputation points">354</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GregRetro has 3 accepted answers">50%</span> </br></p>
</div>
</div>
<div id="comments-container-83621" class="comments-container">
<span id="83771"></span>
<div id="comment-83771" class="comment">
<div id="post-83771-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you supply a link to a functioning example of your routine covering an area which contains examples of the objects you want returned. Provide a specific link to an object that doesn't get returned.</p>
</div>
<div id="comment-83771-info" class="comment-info">
<span class="comment-age">(09 Mar '22, 19:56)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-83621" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83621-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

