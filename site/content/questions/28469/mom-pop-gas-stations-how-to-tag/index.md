+++
type = "question"
title = "Mom &amp; pop gas stations, how to tag?"
description = '''I am mapping in Thailand and frequently need to add small fuel stops to the local map. These are small shops in out of the way places that sell petrol by the bottle or pumped from a large drum or barrel manually. The customers mostly drive motorcycles and this service is very useful to them. And to ...'''
date = "2013-11-26T05:18:00Z"
lastmod = "2017-01-03T23:13:00Z"
weight = 28469
keywords = [ "fuel", "tagging" ]
aliases = [ "/questions/28469" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Mom & pop gas stations, how to tag?](/questions/28469/mom-pop-gas-stations-how-to-tag)

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
<span id="post-28469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28469-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am mapping in Thailand and frequently need to add small fuel stops to the local map. These are small shops in out of the way places that sell petrol by the bottle or pumped from a large drum or barrel manually. The customers mostly drive motorcycles and this service is very useful to them. And to me, on occasion.</p>
<p>These shops are scattered here and there in remote areas of Thailand and are a useful amenity if you're running low on gas and are 50-60 km from a larger town.</p>
<p>The question is, how to tag them? Some folks use a combination of amenity=fuel name=barreled fuel so they a) show up on a GPS and b) the name will indicate that it is not a normal refueling shop. This is what I've been doing lately.</p>
<p>Suggestions?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-fuel" rel="tag" title="see questions tagged &#39;fuel&#39;">fuel</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Nov '13, 05:18</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-28469" class="comments-container">
<span id="28485"></span>
<div id="comment-28485" class="comment">
<div id="post-28485-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>meta: I think that it would be better to discuss new tags <span>somewhere</span> else but here (help site). In pure theory just the general questions "how can I find tags" and "there seems to be no suitable tag, what now?" should be here (and surely are <span>somewhere</span>). E.g. <span>which-tags-do-i-use</span>. Yes, practically it is done differently here. ;-)</p>
</div>
<div id="comment-28485-info" class="comment-info">
<span class="comment-age">(26 Nov '13, 14:04)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-28469" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28469-form-container" class="comment-form-container">
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

<span id="28486"></span>

<div id="answer-container-28486" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28486-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><span>any tags you like</span> – invent a new tag if you cannot find suitable existing ones and you think it is useful to have. I am not sure if it should be a subkey of <span><code>fuel</code></span> - e.g. <del><code>fuel:selling_type=barrel</code></del> <span class="small">(not a good tag value, could also get used for stations selling whole barrels to customers … that is why discussion is good – someone might mention such problems)</span> <code>fuel:selling_type=hand-pumped</code> or <code>=small_amounts</code> or <code>=barrel_with_handpump</code>, I am not sure what would be really good. It should resemble the relevant features.</p>
<p>Another problem with the aforementioned idea is that it is meant as an addition to <span><code>amenity=fuel</code></span>. That means that all applications which do not understand <code>fuel:selling_type</code> (and default to ignore it) would show the object as a normal gas station which might be problematic for some users. I am not sure if those mini gas stations should be treated as a kind of gas station (amenity=fuel). However, as said, I think it is best discussed in more length somewhere else.</p>
<p>In any case, use the <span><code>description</code></span> tag to make clear what you mean in freeform natural text. You may also find some inspiration at <a href="/questions/27300/">pop-up-shops-mobile-vans-how-to-tag</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '13, 14:04</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Nov '13, 01:09</strong> </span></p>
</div>
</div>
<div id="comments-container-28486" class="comments-container">
<span id="53825"></span>
<div id="comment-53825" class="comment">
<div id="post-53825-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would go with shop=fuel for "a little shop that only sells fuel" or shop=* + vending=fuel for "a little shop where you can buy stuff, including fuel".</p>
</div>
<div id="comment-53825-info" class="comment-info">
<span class="comment-age">(03 Jan '17, 12:14)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="53827"></span>
<div id="comment-53827" class="comment">
<div id="post-53827-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10142/joost-schouppe"></a><a href="http://help.openstreetmap.org/users/10142/joost-schouppe">@joost</a>, I've settled on keeping the amenity=fuel tag and adding a special description tag to distinguish these places from full-service stations. I also have special icon that shows up on my custom maps.</p>
<p>I identify those shops with the description "A small shop or shed selling motor fuel pumped from a barrel or in one-liter bottles", and then in my style file I test for the presence of "shed" in the description. It's a bit weird but it works. I was going to add the shop=fuel tag to the shops page in the Wiki but didn't want to spend the time. Every time I try to add or edit that blasted wiki I get frustrated and give up.</p>
<p>Thanks for your reply. I think your solution is the best one and it is the one we came up with on the tagging forum. I just never added it to the shops page.</p>
<p>Happy New Year</p>
</div>
<div id="comment-53827-info" class="comment-info">
<span class="comment-age">(03 Jan '17, 12:48)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="53837"></span>
<div id="comment-53837" class="comment">
<div id="post-53837-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, I'll try and find a picture of such a place and edit the wiki. Do you happen to have a reference to the tagging forum discussion you mentioned?</p>
</div>
<div id="comment-53837-info" class="comment-info">
<span class="comment-age">(03 Jan '17, 17:57)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="53850"></span>
<div id="comment-53850" class="comment">
<div id="post-53850-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/2850/joostenmies">@Joost</a> - I will send an email containing the Tagging discussion and other details, including a photo of a fuel shop, to your gmail address. Many thanks for your interest.</p>
</div>
<div id="comment-53850-info" class="comment-info">
<span class="comment-age">(03 Jan '17, 23:13)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-28486" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28486-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28474"></span>

<div id="answer-container-28474" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28474-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use brand=barreled_fuel instead of the name of an multinational, the name tag could then be used for the owner, with telephone=1234567 on option just to ask if there’s fuel available ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '13, 10:48</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-28474" class="comments-container">
<span id="28480"></span>
<div id="comment-28480" class="comment">
<div id="post-28480-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I guess because brand=barreled_fuel doesn't show up as such on my GPS. And labeling it either way, as brand or name, is incorrect anyway. I realize I'm guilty of tagging for the renderer but I don't want to ignore these valuable resources just because there's no proper way to tag them. At any rate, these are not shop owners that I can stop and interview. For one thing, they speak Thai and I do not. I spot them as I drive by and take a photo which I later geolocate and add to the OSM of the area. There are no signs and nobody would call ahead to see if the shop is open.</p>
<p>Thanks for your input.</p>
</div>
<div id="comment-28480-info" class="comment-info">
<span class="comment-age">(26 Nov '13, 12:46)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="28490"></span>
<div id="comment-28490" class="comment">
<div id="post-28490-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@Hendrikklaas</span> - "barrelled" isn't really a brand in the way that Petronas or Shell is, is it?</p>
<p><span>@AlaskaDave</span> - if it doesn't show up on your (I'm assuming Garmin) GPS perhaps it's worth creating your own maps and editing the mkgmap style file so that they do?</p>
</div>
<div id="comment-28490-info" class="comment-info">
<span class="comment-age">(26 Nov '13, 14:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="28491"></span>
<div id="comment-28491" class="comment">
<div id="post-28491-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>… An export (e.g. by <a href="http://overpass-turbo.eu/?key=fuel:selling_type&amp;value=barrel&amp;template=key-value">overpass-turbo</a>) of all such gas stations into an gpx waypoint file may be sufficient, too. … to be added on top of some other map.</p>
</div>
<div id="comment-28491-info" class="comment-info">
<span class="comment-age">(26 Nov '13, 14:46)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="28512"></span>
<div id="comment-28512" class="comment">
<div id="post-28512-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Correct, barreled is no specific brand. But I expect several no named stations but no brand ones in rural areas selling white unnamed fuel. Barreled seems to be a better one, then bottled isn’t it ? When used it could be added to the WIKI in time. And yes they will be small business for ever as well.</p>
</div>
<div id="comment-28512-info" class="comment-info">
<span class="comment-age">(26 Nov '13, 23:34)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="28515"></span>
<div id="comment-28515" class="comment">
<div id="post-28515-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@SomeoneElse</span>: yes, that's the ultimate answer to at least one of my particular problems. I have gone through the process once and found it doable but daunting. I imagine any venture into creating my own styles will be similar.</p>
<p>Moreover, these shops are useful to have on the general OSM map as they offer fuel in places where the big distributors do not.</p>
</div>
<div id="comment-28515-info" class="comment-info">
<span class="comment-age">(27 Nov '13, 00:39)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-28474" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28474-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28516"></span>

<div id="answer-container-28516" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28516-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>How about this:</p>
<p>amenity=fuel</p>
<p>ownership=private (7500 exist)</p>
<p>description:en=a small shop selling fuel pumped from a barrel, no other services available and usually having no sign.</p>
<p>I would create a preset for use in JOSM for the sake of consistency.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Nov '13, 01:02</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-28516" class="comments-container">
<span id="28517"></span>
<div id="comment-28517" class="comment">
<div id="post-28517-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@AlaskaDave</span>: I do not see the distinction here. "private" are all except some state-owned gas stations (maybe in some countries). The description is good.</p>
</div>
<div id="comment-28517-info" class="comment-info">
<span class="comment-age">(27 Nov '13, 01:12)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="28518"></span>
<div id="comment-28518" class="comment">
<div id="post-28518-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@aseerel</span>- Yes, of course, you're correct. Back to the drawing board I reckon. Maybe just not use the owner tag but leave all else as is?</p>
<p>That would work for now.</p>
</div>
<div id="comment-28518-info" class="comment-info">
<span class="comment-age">(27 Nov '13, 01:42)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-28516" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28516-form-container" class="comment-form-container">
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

