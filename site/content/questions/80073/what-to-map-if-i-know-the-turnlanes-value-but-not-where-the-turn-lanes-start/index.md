+++
type = "question"
title = "What to map if I know the turn:lanes value but not where the turn lanes start?"
description = '''The documentation for turn:lanes says the tag should be applied &quot;from the first indication ... to the junction&quot;. What if I know the lane turning indications but not the position along the road where they start (for example, the position where the road widens with the addition of the turn lanes)? Is ...'''
date = "2021-05-08T20:29:00Z"
lastmod = "2021-09-06T17:47:00Z"
weight = 80073
keywords = [ "turnlanes" ]
aliases = [ "/questions/80073" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What to map if I know the turn:lanes value but not where the turn lanes start?](/questions/80073/what-to-map-if-i-know-the-turnlanes-value-but-not-where-the-turn-lanes-start)

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
<span id="post-80073-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80073-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80073-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Key:turn">The documentation for <code>turn:lanes</code></a> says the tag should be applied "from the first indication ... to the junction". What if I know the lane turning indications but not the position along the road where they start (for example, the position where the road widens with the addition of the turn lanes)? Is there a way I can usefully contribute this information to the map? Often, during a trip I'm taking for another reason, I can remember the turning indications but I don't want to go to the extra trouble to try to record the starting position.</p>
<p>So far, I've been adding the <code>turn:lanes</code> tag to the last way before the junction, which may be short or long depending on how the road is currently segmented on OSM (which would depend on what segments needed to be tagged differently for other reasons). In effect, I was thinking of the <code>turn:lanes</code> tag as applying to the <em>end</em> of the way. I believed that even if my practice didn't follow the standard, it was still better than not having the data. And indeed, the main router that I use (OsmAnd) showed the same lane guidance regardless of the length of the last way, as long as it didn't extend beyond the previous junction. But I recently realized that two problems can occur if the way extends beyond the previous junction, which is the case with <a href="https://www.openstreetmap.org/way/76696898">one way I recently changed</a> (at version 5):</p>
<ol>
<li>If a route includes a turn at the previous junction, OsmAnd shows lane guidance based on my <code>turn:lanes</code> value there even though it was not intended to apply to the previous junction.</li>
<li>If another user later splits the way, the editor may copy the tag to both new ways, and the fact that I intended it to apply only to the second way would be forgotten.</li>
</ol>
<p>So now I'm wondering both how I should fix my previous edits and what I should do in the future if I know the turn indications but not where they start. In some cases, I may be able to get the starting point from imagery, but not in all cases. Would the following be reasonable: add the tag to the last way, but if that way extends beyond the previous junction, split it there before adding the tag to the second part? Then is there a way I can record for other mappers (e.g., in a <code>note</code> tag) the fact that I didn't know the real starting point, so that if they do know it, they know it's safe to overwrite my data? (If it would be better to take this discussion to another place, such as the "tagging" mailing list, I'm open to doing so.)</p>
<p>For that matter, is <code>turn:lanes</code> data on OpenStreetMap valuable enough that I should even bother to collect it and address this question in the first place?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-turnlanes" rel="tag" title="see questions tagged &#39;turnlanes&#39;">turnlanes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 May '21, 20:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a09c08e1ae93a83e9102b6715fc75b4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Matt%20McCutchen&#39;s gravatar image" />
<p><span>Matt McCutchen</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Matt McCutchen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80073" class="comments-container">
<span id="80074"></span>
<div id="comment-80074" class="comment">
<div id="post-80074-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Out of curiosity: How are you able to identify the turn lanes without knowing where they start?</p>
</div>
<div id="comment-80074-info" class="comment-info">
<span class="comment-age">(08 May '21, 22:50)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="80075"></span>
<div id="comment-80075" class="comment">
<div id="post-80075-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As I'm moving, I can see where the lanes start, but I have no way to locate the point precisely on the map. Even if my phone is recording a GPS trace, if I'm driving, I may not have a free hand to push a button to make a mark at the current location, or even if I did, the latency of my GPS receiver may make it hard to get an accurate location.</p>
</div>
<div id="comment-80075-info" class="comment-info">
<span class="comment-age">(08 May '21, 23:14)</span> <span class="comment-user userinfo">Matt McCutchen</span>
</div>
</div>
</div>
<div id="comment-tools-80073" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80073-form-container" class="comment-form-container">
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

<span id="80076"></span>

<div id="answer-container-80076" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80076-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-80076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As you have discovered, <code>turn:lanes</code> tagging applies to the entire length of a way. There may be some applications (e.g. lane guidance in some routing software) where this distinction doesn't have a visible effect, but it does matter for other use cases. For example, a renderer with support for lanes will display the turn lanes along the entire length of the way.</p>
<p>Of course, it would be ideal if you could make out the start of the turn lanes on the aerial imagery background or with street-level images that are permitted for use in OSM mapping (e.g. Mapillary, KartaView) and split the way in that location.</p>
<p>If that's not possible, though, you could split the way quite close to the junction and tag only the short bit immediately adjacent to the junction with <code>turn:lane</code> information. This reflects the knowledge you actually have: Only the last bit before the junction will have lane information, because that's what you remember. Lane information for the rest of the street will remain untagged and thus unknown. If a future mapper figures out the exact location where the turn lanes start, they can move the split node (or merge the short way back with the longer section as needed).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 May '21, 23:39</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 May '21, 23:39</strong> </span></p>
</div>
</div>
<div id="comments-container-80076" class="comments-container">
<span id="80077"></span>
<div id="comment-80077" class="comment">
<div id="post-80077-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks. As a newcomer, I assumed that artificially splitting ways was undesirable, but if you don't think it's a big deal, I'll go with that solution for now. Maybe I'll invent a tag, <code>fixme:turn:lanes:start=resurvey</code>, to indicate that the starting point of the <code>turn:lanes</code> is unknown.</p>
</div>
<div id="comment-80077-info" class="comment-info">
<span class="comment-age">(09 May '21, 01:31)</span> <span class="comment-user userinfo">Matt McCutchen</span>
</div>
</div>
<span id="80085"></span>
<div id="comment-80085" class="comment">
<div id="post-80085-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think a textual fixme tag would be better, like fixme="start of turn lane imprecise". If you invent a new tag it won't be displayed by any tool.</p>
</div>
<div id="comment-80085-info" class="comment-info">
<span class="comment-age">(09 May '21, 18:41)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="80247"></span>
<div id="comment-80247" class="comment">
<div id="post-80247-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Adding nodes to change geometry is normal. Splitting the way at a node is necessary when way information is different for each side of the way. If you are mapping lane information, you will be doing this regularly unless working in an area where it has already been done. If you have data that likely needs correction such as guessing at the location the turn lane starts then you could use a fixme or a map note to draw attention/reminder to it. If you plan to fix in short order they make it easy to find and you can even note there that you will resurvey it but if not then other mappers can take what is there to further revise it. New tags are best when trying to present something that doesn't fit current tagging. New tags are worth documenting and discussing so people can be aware of them and may have feedback to further improve the idea. I don't know if anyone looks out for fixme: tags but editors definitely draw attention to fixme itself. You could store the entire information within the fixme message if you felt that what you were about to add could be wrong data; someone could copy it into proper tags when ready.</p>
</div>
<div id="comment-80247-info" class="comment-info">
<span class="comment-age">(20 May '21, 20:28)</span> <span class="comment-user userinfo">mirror176</span>
</div>
</div>
<span id="81644"></span>
<div id="comment-81644" class="comment">
<div id="post-81644-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the further advice. (Somehow I did not get email notifications for the last two comments.) As of now, I've been able to collect the missing information to eliminate all my existing <code>fixme:turn:lanes:start=resurvey</code> tags. If I have the same situation in the future, I'll use <code>fixme</code> with a textual explanation for the time being; I'll wait to propose a structured tag for informal standardization until it seems worth it. I get the sense that making map notes for small things like this will just clutter the set of notes and make it harder for users to find more important notes; if OSM had a better system for categorizing notes, that would help, though using <code>fixme</code> tags and searching for them is probably a decent solution too.</p>
</div>
<div id="comment-81644-info" class="comment-info">
<span class="comment-age">(06 Sep '21, 17:47)</span> <span class="comment-user userinfo">Matt McCutchen</span>
</div>
</div>
</div>
<div id="comment-tools-80076" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80076-form-container" class="comment-form-container">
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

