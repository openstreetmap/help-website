+++
type = "question"
title = "Mapping boardwalks and bridges - help needed."
description = '''Hi all, Early last week I mapped some footpaths around a man-made lake and for the first time attempted to map both a bridge and a number of boardwalks at this same location. The footpaths started to show on OSM in a matter of minutes but even now, several days later, neither the bridge nor the boar...'''
date = "2015-07-05T12:44:00Z"
lastmod = "2015-07-07T09:28:00Z"
weight = 43989
keywords = [ "bridge", "boardwalk", "help" ]
aliases = [ "/questions/43989" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mapping boardwalks and bridges - help needed.](/questions/43989/mapping-boardwalks-and-bridges-help-needed)

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
<span id="post-43989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43989-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, Early last week I mapped some footpaths around a man-made lake and for the first time attempted to map both a bridge and a number of boardwalks at this same location. The footpaths started to show on OSM in a matter of minutes but even now, several days later, neither the bridge nor the boardwalks are showing on the map except when I view OSM from the basic in browser editor, the link at the bottom of the left hand side of the screen, "View on openstreetmap.org". Even more confusing to me is that in the basic editor my 'bridge' is shown as a Line with the tags 'bridge=yes' but in Potlatch2 it reads "not recognised" and 'unknown' and also tags: bridge=yes(edit). I assume that I've done something wrong. Will someone please help?</p>
<p>Regards,</p>
<p>biggles</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span> <span class="post-tag tag-link-boardwalk" rel="tag" title="see questions tagged &#39;boardwalk&#39;">boardwalk</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jul '15, 12:44</strong></p>
<img src="https://secure.gravatar.com/avatar/08a89d472ef0fd8ab6e5062ff22ed08a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="biggles1024&#39;s gravatar image" />
<p><span>biggles1024</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="biggles1024 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43989" class="comments-container">
&#10;</div>
<div id="comment-tools-43989" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43989-form-container" class="comment-form-container">
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

<span id="43992"></span>

<div id="answer-container-43992" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43992-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43992-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-43992-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I guess you are talking about <a href="https://www.openstreetmap.org/#map=18/-38.10181/145.32595">this area</a>.</p>
<p>The bridges you have added (e.g. <a href="https://www.openstreetmap.org/way/357315736">way 357315736</a>) only have a <em>bridge=yes</em> tag. You forgot to add the highway tag, in this case <em>highway=footway</em>. The same applies for your <a href="https://www.openstreetmap.org/way/356864876">boardwalk</a>. There is even a <a href="https://www.openstreetmap.org/way/357366943">boardwalk</a> with no bridge at all, instead it is tagged with <em>Line=boardwalk</em> which is no valid tag.</p>
<p>After correcting these mistakes your bridges and boardwalks should start getting rendered.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jul '15, 13:27</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-43992" class="comments-container">
<span id="43998"></span>
<div id="comment-43998" class="comment">
<div id="post-43998-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank-you so much. I can see now that it is in a sense, a two-step process. What I tagged as a boardwalk is a timber surface that starts off flush with the concrete footpath and rises to no more than around 800mm from the ground. The ground under is garden and there are no handrails along the sides. The bridge on the other hand spans a section of the lake/pond, is quite a bit higher and does have handrails on both sides. I've made the changes you advised and will now sit back and wait and see what happens. Thanks again for your help.</p>
</div>
<div id="comment-43998-info" class="comment-info">
<span class="comment-age">(05 Jul '15, 22:19)</span> <span class="comment-user userinfo">biggles1024</span>
</div>
</div>
<span id="43999"></span>
<div id="comment-43999" class="comment">
<div id="post-43999-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Since you mentioned handrails: You can add this information, too. Just take a look at the <a href="https://wiki.openstreetmap.org/wiki/Key:handrail">handrail tag</a> in the wiki :). And another thing: For proper routing please connect your footways to the surrounding highways. Currently not all ends of the footway are properly connected. <a href="https://www.openstreetmap.org/way/357296349">Way 357296349</a> even ends at an administrative boundary which you seem to have mistaken for a routable way.</p>
</div>
<div id="comment-43999-info" class="comment-info">
<span class="comment-age">(06 Jul '15, 07:41)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44002"></span>
<div id="comment-44002" class="comment">
<div id="post-44002-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the advice RE handrails. I have yet to determine exactly where the footpaths connect to the roads and how to do it. I am planning on return during the next couple of days depending in the weather. Its the middle of winter here. ;)</p>
</div>
<div id="comment-44002-info" class="comment-info">
<span class="comment-age">(06 Jul '15, 12:19)</span> <span class="comment-user userinfo">biggles1024</span>
</div>
</div>
<span id="44003"></span>
<div id="comment-44003" class="comment">
<div id="post-44003-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've looked for this too, and haven't found a well defined way to tag boardwalks on the wiki beyond surface=wood. I have seen that some people add bridge=boardwalk to the footway, whether it is over open water or not. See also <a href="/questions/31231/how-do-i-tag-footpaths-made-of-wood">https://help.openstreetmap.org/questions/31231/how-do-i-tag-footpaths-made-of-wood</a></p>
</div>
<div id="comment-44003-info" class="comment-info">
<span class="comment-age">(06 Jul '15, 14:47)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="44010"></span>
<div id="comment-44010" class="comment">
<div id="post-44010-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/595/neuhausr">@neuhausr</a>: The wiki page for [bridge=boardwalk] does not require the bridge to be over open water. The definition states "A plank walkway over wet or otherwise difficult terrain, usually low to the ground and supported by posts."</p>
</div>
<div id="comment-44010-info" class="comment-info">
<span class="comment-age">(06 Jul '15, 20:15)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="44011"></span>
<div id="comment-44011" class="comment not_top_scorer">
<div id="post-44011-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5390/escada">@escada</a>, exactly my point! :)</p>
</div>
<div id="comment-44011-info" class="comment-info">
<span class="comment-age">(06 Jul '15, 20:39)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="44022"></span>
<div id="comment-44022" class="comment not_top_scorer">
<div id="post-44022-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, or this one <a href="https://www.openstreetmap.org/#map=19/52.94626/6.46945">https://www.openstreetmap.org/#map=19/52.94626/6.46945</a><br />
not a bridge at all but a stretch of beams covering the underlaying peat, next to eachother, "bridge" just like the Romans build theyre ways in wet areas or "boardwalk" ? This ones carries a tag as, historic=archeological_site</p>
</div>
<div id="comment-44022-info" class="comment-info">
<span class="comment-age">(07 Jul '15, 09:28)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-43992" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-43992-form-container" class="comment-form-container">
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

