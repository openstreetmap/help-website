+++
type = "question"
title = "Ecuador: cleaning up an address mess"
description = '''There&#x27;s quite a tagging mess here, mostly due to people not thinking about what a name is: https://forum.openstreetmap.org/viewtopic.php?id=69184 I culled a few obviously nonsensical names such as &quot;solar vacio&quot; (&quot;empty lot&quot;) already but for the rest I&#x27;d like to hear what others think. The V-somethin...'''
date = "2020-10-02T10:05:00Z"
lastmod = "2020-10-03T07:31:00Z"
weight = 76925
keywords = [ "name", "ecuador", "address" ]
aliases = [ "/questions/76925" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Ecuador: cleaning up an address mess](/questions/76925/ecuador-cleaning-up-an-address-mess)

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
<span id="post-76925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76925-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There's quite a tagging mess here, mostly due to people not thinking about what a name is: <a href="https://forum.openstreetmap.org/viewtopic.php?id=69184">https://forum.openstreetmap.org/viewtopic.php?id=69184</a> I culled a few obviously nonsensical names such as "solar vacio" ("empty lot") already but for the rest I'd like to hear what others think.</p>
<p>The V-something "names" seem to be actual house numbers while most of these buildings are tagged with <code>addr:housenumber</code> being "MZ-something" for "manzana", block. So I guess the possibilities are a) always use the combination of manzana and number as <code>addr:housenumber=MZx n</code> b) <code>addr:block=m</code> without the MZ prefix, <code>addr:housenumber=n</code>, probably best without the V c) <code>addr:place</code> instead of <code>addr:block</code> - I understand the block number is supposed to be used instead of <code>addr:street</code> while the manzana isn't useful without a street. I'm leaning towards b).</p>
<p>Orthogonal to that: would a building name like "Condominio Geminis" go into "name" or <code>addr:housename</code>? The latter is not considered mutually exclusive with <code>addr:housenumber</code>, is it?</p>
<p>Then again, is it worth cleaning that up in the first place, considering many of those "buildings" don't correspond to real-world buildings but rather to something like lots? Maybe deleting the <code>building=*</code> where the subjective difference between the building outline and mapped area is too big?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-ecuador" rel="tag" title="see questions tagged &#39;ecuador&#39;">ecuador</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Oct '20, 10:05</strong></p>
<img src="https://secure.gravatar.com/avatar/d62eaa0c9cab6317d2887bfe6bd2163b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mbethke&#39;s gravatar image" />
<p><span>mbethke</span><br />
<span class="score" title="381 reputation points">381</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mbethke has 2 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-76925" class="comments-container">
<span id="76927"></span>
<div id="comment-76927" class="comment">
<div id="post-76927-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't know enough about that type of addressing scheme to comment, but I do want to comment on the house name aspect. addr:housename is for when the name of the building is part of the mailing address (usually because the building doesn't have a addr:housenumber, so the name is the only way to identify the correct delivery location). In the case of "Condominio Geminis", that sounds like a name=*, not part of the address.</p>
</div>
<div id="comment-76927-info" class="comment-info">
<span class="comment-age">(02 Oct '20, 17:44)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="76928"></span>
<div id="comment-76928" class="comment">
<div id="post-76928-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, that's sort of my gut feeling, too. The building name <em>is</em> commonly used as part of the address; my memory of Ecuador is too hazy to tell whether there are cases where where several buildings of different name use the same house number but I think the name is generally just a more mailman-friendly extra.</p>
</div>
<div id="comment-76928-info" class="comment-info">
<span class="comment-age">(03 Oct '20, 07:31)</span> <span class="comment-user userinfo">mbethke</span>
</div>
</div>
</div>
<div id="comment-tools-76925" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76925-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

