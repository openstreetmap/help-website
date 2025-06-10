+++
type = "question"
title = "Tagging a combined shop of optician and hearing aids"
description = '''In my area there are shops which sell both optics such as glasses and contact lenses as well as hearing aids. How should I tag them? I could go for shop=optician;hearing_aids. But then my question is if the shop will be found by data users? This combination appears only 29 times (and 11 times the ot...'''
date = "2020-03-11T21:04:00Z"
lastmod = "2020-03-12T14:56:00Z"
weight = 73478
keywords = [ "shop", "multiple", "optician", "tagging", "semicolon" ]
aliases = [ "/questions/73478" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Tagging a combined shop of optician and hearing aids](/questions/73478/tagging-a-combined-shop-of-optician-and-hearing-aids)

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
<span id="post-73478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73478-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In my area there are shops which sell both optics such as glasses and contact lenses as well as hearing aids. How should I tag them?</p>
<p>I could go for <code>shop=optician;hearing_aids</code>. But then my question is if the shop will be found by data users? This combination appears only 29 times (and 11 times the other way round) globally according to <a href="https://taginfo.openstreetmap.org/tags/shop=optician%3Bhearing_aids">taginfo</a>.</p>
<p>Or I could subjectively choose which one seems to be the main business and tag e.g. as <a href="https://wiki.openstreetmap.org/wiki/Tag:shop%3Doptician"><code>shop=optician</code></a> and add a note about the hearing aids in a <a href="https://wiki.openstreetmap.org/wiki/Key:description"><code>description</code></a> tag.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shop" rel="tag" title="see questions tagged &#39;shop&#39;">shop</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-optician" rel="tag" title="see questions tagged &#39;optician&#39;">optician</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-semicolon" rel="tag" title="see questions tagged &#39;semicolon&#39;">semicolon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Mar '20, 21:04</strong></p>
<img src="https://secure.gravatar.com/avatar/97f754e0356a74acc666550948b48bd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hfs&#39;s gravatar image" />
<p><span>hfs</span><br />
<span class="score" title="851 reputation points">851</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hfs has 3 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-73478" class="comments-container">
&#10;</div>
<div id="comment-tools-73478" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73478-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="73485"></span>

<div id="answer-container-73485" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73485-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-73485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hfs has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's a semi-official rule, and definitely general best practice, to avoid semicolon-separted values on "top-level" POI tags such as amenity, shop, and office. See <a href="https://wiki.openstreetmap.org/wiki/Semi-colon_value_separator#When_NOT_to_use">https://wiki.openstreetmap.org/wiki/Semi-colon_value_separator#When_NOT_to_use</a></p>
<p>My suggestion would be to make a call as to which is the primary purpose of the shop. If it's optical, then tag <strong><code>shop=optician</code></strong> + <strong><code>heading_aids=yes</code></strong>, and visa-versa.</p>
<p>Sometimes it's a hard call to make, but I still believe that going with one over the other is a better call than a semicoloned value.</p>
<p>It might also a good idea to add a description tag that mentions the multiple purposes of the shop, because some software may use <strong><code>description=</code></strong> but not look for various <strong><code>*=yes</code></strong> tags.</p>
<p>Other commonly paired shops: coffee/tea, tattoo/piercing/jewelry, bakery/pastry, convenience/tobacco. When I see these I choose one value for <strong><code>shop=</code></strong> and put the other as a key with value <strong><code>yes</code></strong>.</p>
<p>It's worth noting that there are some shop types where using the equivalent <strong><code>*=yes</code></strong> might be confusing, for example <strong><code>bicycle=yes</code></strong> is usually an access tag, <strong><code>pet=yes</code></strong> usually refers to permission to bring pets to a POI (though <strong><code>pets=yes</code></strong> is more common for this purpose.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Mar '20, 23:08</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-73485" class="comments-container">
<span id="73491"></span>
<div id="comment-73491" class="comment">
<div id="post-73491-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To me listing a plain <code>item=yes</code> is rather more concerning in the difficulty to interpret and support in general. A <code>feature:item=yes</code> or <code>item:activity=yes</code> would allow <code>item</code> to be put as an option available under <code>feature</code>, aside from less confusion with various <code>feature</code>. Although, as someone who appreciates namespacing I'm still wary of its possible limitations</p>
<p>As a side note, medical devices can have access restrictions . For example, implanted cardiac devices (eg icd, artificial pacemaker) require magnetic shielding to protect against electromagnetic fields.</p>
</div>
<div id="comment-73491-info" class="comment-info">
<span class="comment-age">(12 Mar '20, 08:20)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="73495"></span>
<div id="comment-73495" class="comment">
<div id="post-73495-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I agree that <strong><code>*=yes</code></strong> is a less-than-ideal solution, but it's most widely implemented.</p>
<p>For shops, the best-supported namespace tagging would probably be eg <strong><code>sells:hearing_aids=yes</code></strong>, which would be a lot easier for software to parse (versus iterating through <strong><code>*=yes</code></strong> and guessing which ones refer to secondary shop purposes.) But "please don't list everything that a shop sells/every item on a restaurant menu/etc" is another traditional OSM best practice, so it hasn't gained a lot of traction.</p>
<p>There's also some support for using <strong><code>shop_1=*</code></strong> and <strong><code>alt_shop=*</code></strong> for secondary shop purposes. <strong><code>alt_shop=*</code></strong> would actually be my preferred solution to this problem, but it's so rarely used that it's barely worth mentioning.</p>
<p>Using tobacco as an example:</p>
<ul>
<li><strong><code>tobacco=yes</code></strong>, 2 371 uses</li>
<li><strong><code>sells:tobacco=yes</code></strong>, 174 uses</li>
<li><strong><code>shop_1=tobacco</code></strong>, 115 uses</li>
<li><strong><code>alt_shop=tobacco</code></strong>, 0 uses (the most common is <strong><code>alt_shop=beauty</code></strong> at 31 uses)</li>
</ul>
</div>
<div id="comment-73495-info" class="comment-info">
<span class="comment-age">(12 Mar '20, 14:56)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-73485" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73485-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73492"></span>

<div id="answer-container-73492" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73492-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is worth considering <code>craft=optician</code> or <code>craft=hearing_aid</code> if either is "crafted" to some degree on site (keeping the possible ambiguity of <code>shop=</code> vs <code>craft=</code> in mind), and <code>healthcare=optometrist</code> or <code>healthcare=audiobiologist</code> if a practicing registered medical specialist is at the shop.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '20, 08:32</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Mar '20, 08:46</strong> </span></p>
</div>
</div>
<div id="comments-container-73492" class="comments-container">
&#10;</div>
<div id="comment-tools-73492" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73492-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73493"></span>

<div id="answer-container-73493" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73493-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've seen a few bakery/convenience combination tagged as two separated nodes on the same building. It feels a bit silly to duplicate name, contact and opening_hours, but I guess it's the easiest for data cousumer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '20, 10:44</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-73493" class="comments-container">
&#10;</div>
<div id="comment-tools-73493" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73493-form-container" class="comment-form-container">
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

