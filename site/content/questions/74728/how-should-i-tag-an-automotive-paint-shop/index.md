+++
type = "question"
title = "How should I tag an automotive paint shop?"
description = '''There exists a business that deals with motor vehicles, but apparently only does paint jobs. There doesn&#x27;t seem to be any specific shop=* value for this--perhaps there&#x27;s a way to specify under an existing tag?'''
date = "2020-05-11T09:35:00Z"
lastmod = "2020-05-12T12:28:00Z"
weight = 74728
keywords = [ "shop", "paint", "motor_vehicle" ]
aliases = [ "/questions/74728" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How should I tag an automotive paint shop?](/questions/74728/how-should-i-tag-an-automotive-paint-shop)

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
<span id="post-74728-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74728-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74728-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There exists a business that deals with motor vehicles, but apparently only does paint jobs. There doesn't seem to be any specific <code>shop=*</code> value for this--perhaps there's a way to specify under an existing tag?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shop" rel="tag" title="see questions tagged &#39;shop&#39;">shop</span> <span class="post-tag tag-link-paint" rel="tag" title="see questions tagged &#39;paint&#39;">paint</span> <span class="post-tag tag-link-motor_vehicle" rel="tag" title="see questions tagged &#39;motor_vehicle&#39;">motor_vehicle</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 May '20, 09:35</strong></p>
<img src="https://secure.gravatar.com/avatar/318c1da3c99b1d25f9834cbb24648736?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zismac&#39;s gravatar image" />
<p><span>Zismac</span><br />
<span class="score" title="136 reputation points">136</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zismac has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74728" class="comments-container">
<span id="74736"></span>
<div id="comment-74736" class="comment">
<div id="post-74736-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'd look at craft offerings. These are basically a service rather than a retail outlet. Alternative car_repair.</p>
</div>
<div id="comment-74736-info" class="comment-info">
<span class="comment-age">(11 May '20, 13:23)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="74748"></span>
<div id="comment-74748" class="comment">
<div id="post-74748-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/647/sk53"></a><a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a> <code>craft=car_painter</code> has 44 uses according to taginfo, would that do the trick? Although I am somewhat concerned by that tag being specific to cars, when this shop services any type of motor vehicle...</p>
</div>
<div id="comment-74748-info" class="comment-info">
<span class="comment-age">(11 May '20, 22:03)</span> <span class="comment-user userinfo">Zismac</span>
</div>
</div>
</div>
<div id="comment-tools-74728" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74728-form-container" class="comment-form-container">
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

<span id="74741"></span>

<div id="answer-container-74741" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74741-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-74741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Adding <strong><code>service:vehicle:painting=yes</code></strong> to <strong><code>shop=car_repair</code></strong> is reasonably common. In this case, because painting is the only service, you could change the tag to <strong><code>service:vehicle:painting=only</code></strong> -- but this is still questionable tagging IMO, using <strong><code>shop=car_repair</code></strong> when the shop in question does <em>not</em> do repairs.</p>
<p>I'd probably go with <strong><code>shop=car_painting</code></strong>, which according to Taginfo has 3 uses worldwide. So it's a very uncommon tag, but still better than tagging incorrectly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '20, 16:29</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-74741" class="comments-container">
<span id="74749"></span>
<div id="comment-74749" class="comment">
<div id="post-74749-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><code>shop=car_painting</code> seems good, but would it apply to the shop I'm tagging, which services many types of motor vehicles?</p>
</div>
<div id="comment-74749-info" class="comment-info">
<span class="comment-age">(12 May '20, 03:13)</span> <span class="comment-user userinfo">Zismac</span>
</div>
</div>
<span id="74754"></span>
<div id="comment-74754" class="comment">
<div id="post-74754-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/17626/zismac">@Zismac</a> I wouldnt worry too much about whether it is cars or other kinds of vehicles at this stage. OSM works iteratively, so as more of these things get mapped, the actual nuances can be added later. Just use a description tag to convey the extra info. Also there is no harm in using both tags mentioned: there's a difference between paint jobs where the vehicle has been damaged and those for, say, advertising purposes.</p>
</div>
<div id="comment-74754-info" class="comment-info">
<span class="comment-age">(12 May '20, 12:28)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-74741" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74741-form-container" class="comment-form-container">
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

