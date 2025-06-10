+++
type = "question"
title = "How should small reserves be tagged?"
description = '''In New Zealand there are many areas that are officially classified as &quot;local purpose reserves&quot;. While there are some large reserves (such as the Porirua Scenic Reserve), many in Porirua are quite small (the size of neighbourhood parks). In particular, there are some that serve no recreational purpos...'''
date = "2019-12-29T06:32:00Z"
lastmod = "2019-12-30T09:25:00Z"
weight = 72268
keywords = [ "park", "new_zealand", "protected_area", "reserve" ]
aliases = [ "/questions/72268" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How should small reserves be tagged?](/questions/72268/how-should-small-reserves-be-tagged)

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
<span id="post-72268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72268-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In New Zealand there are many areas that are officially classified as "local purpose reserves". While there are some large reserves (such as the Porirua Scenic Reserve), many in Porirua are quite small (the size of neighbourhood parks). In particular, there are some that serve no recreational purpose, such as <a href="https://poriruacity.govt.nz/your-council/city-planning-and-reporting/reserves-management/reserve-search/kotuku-reserve/">Kotuku Reserve</a> and the <a href="https://poriruacity.govt.nz/your-council/city-planning-and-reporting/reserves-management/reserve-search/titahi-bay-road-reserves/">Titahi Bay Road Reserves</a>, but seem to be reserved to maintain the landscape.</p>
<p>I'm wondering if these should be tagged with <code>boundary=protected_area</code>, like some large (environmental) reserves are, or if their insignificance means that other tags, such as <code>landuse=grass</code> or <code>leisure=park</code> are more appropriate.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-park" rel="tag" title="see questions tagged &#39;park&#39;">park</span> <span class="post-tag tag-link-new_zealand" rel="tag" title="see questions tagged &#39;new_zealand&#39;">new_zealand</span> <span class="post-tag tag-link-protected_area" rel="tag" title="see questions tagged &#39;protected_area&#39;">protected_area</span> <span class="post-tag tag-link-reserve" rel="tag" title="see questions tagged &#39;reserve&#39;">reserve</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Dec '19, 06:32</strong></p>
<img src="https://secure.gravatar.com/avatar/318c1da3c99b1d25f9834cbb24648736?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zismac&#39;s gravatar image" />
<p><span>Zismac</span><br />
<span class="score" title="136 reputation points">136</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zismac has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72268" class="comments-container">
<span id="72273"></span>
<div id="comment-72273" class="comment">
<div id="post-72273-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ha, I thought about mentioning <code>boundary=protected_area</code> in your previous question, but gave up after failing to search for the origin of "Local Purpose Reserve".</p>
<p>Interesting these are only zoned as "open space". In my place, there are designated green belt or conservation area specifically.</p>
</div>
<div id="comment-72273-info" class="comment-info">
<span class="comment-age">(29 Dec '19, 09:42)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-72268" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72268-form-container" class="comment-form-container">
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

<span id="72274"></span>

<div id="answer-container-72274" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72274-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72274-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72274-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Zismac has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should look into <code>protect_class=</code> and <code>protection_title=</code> when it comes to <code>boundary=protected_area</code>. Local Purpose Reserves (Environmental and Landscape Protection) could probably be compared with UK's Local Nature Reserve if I'm not mistaken, which is <code>protect_class=7</code>. I have no idea about Local Purpose Reserve (Landscape).</p>
<p>[edit] Apparently the Wiki (what would have thought...) and IUCN are conflicting. Because UK LNRs are protected by national legislation, they should be IUCN Category IV, corresponding to <code>protect_class=4</code>.</p>
<p>If you have no idea like I do, you could still add them as <code>boundary=protected_area</code> with a <code>protection_title</code>, then figure out <code>protect_class=</code> later. Many updated <code>leisure=nature_reserve</code> or added <code>boundary=protected_area</code> do not have a <code>protect_class=</code> tagged yet, or are wrong according to other datasets. The project looks very much a WIP.</p>
<blockquote>
<p>or if their insignificance means that other tags, such as landuse=grass or leisure=park are more appropriate.</p>
</blockquote>
<p>As mentioned by others in your previous question, <code>landuse=grass</code> is ambiguous as to its purpose, thus should be further detailed if you so desire. <code>leisure=park</code> needs to be used as such first.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Dec '19, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Dec '19, 09:20</strong> </span></p>
</div>
</div>
<div id="comments-container-72274" class="comments-container">
<span id="72281"></span>
<div id="comment-72281" class="comment">
<div id="post-72281-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>LNRs are not protected by national legislation: the legislation merely allows them to be designated by a local authority. Much of the protection is not legal, but through ownership and planning policies (this actually also applies in practice to pretty much any of the higher designations in the UK). In general I think the text for Australia probably also applies in the UK: certainly I'd be concerned if people took these IUCN codes at face value.</p>
</div>
<div id="comment-72281-info" class="comment-info">
<span class="comment-age">(29 Dec '19, 17:41)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="72286"></span>
<div id="comment-72286" class="comment">
<div id="post-72286-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That depends on the definition of "legal"... I read they are considered as a nationally established level of protection delegated to local authorities.</p>
</div>
<div id="comment-72286-info" class="comment-info">
<span class="comment-age">(30 Dec '19, 09:25)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-72274" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72274-form-container" class="comment-form-container">
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

