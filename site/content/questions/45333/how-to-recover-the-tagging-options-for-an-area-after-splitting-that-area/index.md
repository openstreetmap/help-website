+++
type = "question"
title = "How to recover the tagging options for an area after splitting that area?"
description = '''Several question have been asked about this in the past ( 1, 2, 3 ), and all answers have been at best dubious and at worst completely mistaken. The problem is that iD, for some unfathomable reason, refuses to offer tags for areas if the feature was not started as an area or has had its &quot;area-type&quot; ...'''
date = "2015-09-17T13:10:00Z"
lastmod = "2015-09-18T01:58:00Z"
weight = 45333
keywords = [ "ideditor", "lines", "area" ]
aliases = [ "/questions/45333" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to recover the tagging options for an area after splitting that area?](/questions/45333/how-to-recover-the-tagging-options-for-an-area-after-splitting-that-area)

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
<span id="post-45333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45333-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-45333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Several question have been asked about this in the past ( <a href="https://help.openstreetmap.org/questions/27591/how-to-combine-several-lines-to-an-area-with-editor-id">1</a>, <a href="https://help.openstreetmap.org/questions/27594/can-you-change-a-closed-line-into-an-area">2</a>, <a href="https://help.openstreetmap.org/questions/25707/area-creation-in-id-continuous-addition-of-points-drops-how-to-continue">3</a> ), and all answers have been at best dubious and at worst completely mistaken.</p>
<p>The problem is that iD, for some unfathomable reason, refuses to offer tags for areas if the feature was not started as an area or has had its "area-type" tags removed. This usually occurs when splitting areas (because you tend to delete the relations that iD create before you tag the new areas) or because any area of significant complexity or size is usually more convenient to create using the line tool. Once the line is closed and you try to tag it, you will be unable to search for the area tag settings, such as natural, landuse or building tag settings. iD simply will never offer them up.</p>
<p>If you have such a closed line that you need to tag using area tags, the only solution (if they can even figure that out) is usually to select an arbitrary tag (you can't even manually type a tag to a new feature <em>because iD forces you to use a preset for a new feature</em>!) an then go in an manually set an area tag.</p>
<p><strong><em>Is there a simpler solution to apply area tags in such a situation?</em></strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-lines" rel="tag" title="see questions tagged &#39;lines&#39;">lines</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Sep '15, 13:10</strong></p>
<img src="https://secure.gravatar.com/avatar/01d01832dff61a6bcf68913f1dc001bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Circeus&#39;s gravatar image" />
<p><span>Circeus</span><br />
<span class="score" title="583 reputation points">583</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Circeus has 2 accepted answers">7%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Sep '15, 16:32</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-45333" class="comments-container">
<span id="45334"></span>
<div id="comment-45334" class="comment">
<div id="post-45334-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The sense of frustration in your question makes it sound like you think you've found a bug. Perhaps have a look at previous discussions at</p>
<p><a href="https://github.com/openstreetmap/iD/issues">https://github.com/openstreetmap/iD/issues</a></p>
<p>to see if there's anything relevant and if not, create a new issue there?</p>
<p>PS: If you want people to help you, it might be better to omit things like "... for some unfathomable reason ..." when you ask for assistance (here, there, or indeed anywhere).</p>
</div>
<div id="comment-45334-info" class="comment-info">
<span class="comment-age">(17 Sep '15, 13:28)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="45339"></span>
<div id="comment-45339" class="comment">
<div id="post-45339-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>use potlatch :) you can use the R key to repeat tags from the last way you touched onto the currently selected one</p>
</div>
<div id="comment-45339-info" class="comment-info">
<span class="comment-age">(17 Sep '15, 14:56)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="45340"></span>
<div id="comment-45340" class="comment">
<div id="post-45340-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This does indeed sound like a bug. iD's handling of areas has always been very odd, especially for users being used to other editors like JOSM or potlatch.</p>
</div>
<div id="comment-45340-info" class="comment-info">
<span class="comment-age">(17 Sep '15, 15:09)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="45343"></span>
<div id="comment-45343" class="comment">
<div id="post-45343-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/595/neuhausr">@neuhausr</a> I actually tend to alternate between them because they do some things more conveniently. E.g. iD is a godsend for separating conjoined or overlapping areas and for rapidly adding addresses. On the other hand, Potlatch is needed for adding distant relationships and (for the reason mentioned above) is usually somewhat more convenient for splitting areas. Also the area of the screen where you can't click because of button or the editor think it's too close to the edge of the editing area is quite a bit smaller or inexistant.</p>
</div>
<div id="comment-45343-info" class="comment-info">
<span class="comment-age">(17 Sep '15, 18:24)</span> <span class="comment-user userinfo">Circeus</span>
</div>
</div>
<span id="45345"></span>
<div id="comment-45345" class="comment">
<div id="post-45345-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/2838/circeus">@Circeus</a> +1 There's definitely things I appreciate about iD, but they're outweighed by annoyances (get that context menu out of my way!) So I tend to only use it for specific tasks, or if forced to (for example, MapRoulette or certain HOT tasks)</p>
</div>
<div id="comment-45345-info" class="comment-info">
<span class="comment-age">(17 Sep '15, 19:08)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-45333" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45333-form-container" class="comment-form-container">
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

<span id="45351"></span>

<div id="answer-container-45351" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45351-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-45351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hey, iD developer here. We do want to make this better, possibly by adding some special presets like "Change to Line" or "Change to Area". Until then:</p>
<p><strong>To turn a line into an area</strong> is easy, just open the raw tag editor and add the tag <code>area=yes</code>. Then you'll have access to the area presets.</p>
<p><strong>To turn an area into a line</strong> is trickier. As before you can use the raw tag editor but you'll need to remove whatever tag is causing it to be an area. It could be <code>area=*</code> or <code>landuse=*</code> or <code>building=*</code> or <code>natural=*</code> or any number of other things.</p>
<p>You said something else:</p>
<p><em>&gt; iD forces you to use a preset for a new feature</em></p>
<p>Yes you are "forced" to pick a preset, but the last suggestion at the bottom of the list is just a generic "Line" preset with no tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '15, 01:58</strong></p>
<img src="https://secure.gravatar.com/avatar/5372740989fdca18458f194a285fcb3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bhousel&#39;s gravatar image" />
<p><span>bhousel</span><br />
<span class="score" title="2089 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bhousel has 13 accepted answers">38%</span></p>
</div>
</div>
<div id="comments-container-45351" class="comments-container">
&#10;</div>
<div id="comment-tools-45351" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45351-form-container" class="comment-form-container">
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

