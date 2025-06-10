+++
type = "question"
title = "How to tag indoor printers?"
description = '''Especially in universities it might be interesting to tag indoor printers accessible to students. How can this be done?'''
date = "2017-12-25T00:09:00Z"
lastmod = "2017-12-26T16:07:00Z"
weight = 61351
keywords = [ "indoor", "university", "printer", "amenity" ]
aliases = [ "/questions/61351" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag indoor printers?](/questions/61351/how-to-tag-indoor-printers)

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
<span id="post-61351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61351-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Especially in universities it might be interesting to tag indoor printers accessible to students. How can this be done?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-indoor" rel="tag" title="see questions tagged &#39;indoor&#39;">indoor</span> <span class="post-tag tag-link-university" rel="tag" title="see questions tagged &#39;university&#39;">university</span> <span class="post-tag tag-link-printer" rel="tag" title="see questions tagged &#39;printer&#39;">printer</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Dec '17, 00:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a27c3ae672bf1df6eb348c3f7ed6a39d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nw520&#39;s gravatar image" />
<p><span>nw520</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nw520 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61351" class="comments-container">
<span id="61359"></span>
<div id="comment-61359" class="comment">
<div id="post-61359-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you suggesting that a printer could be trackable, and plotted on OSM? a bit like the police could track a stolen car? I think osm would take a too long to re-render although looking at the data might work. an interesting way see who has the printer, but it would require users doing the logging at the time, every time.</p>
</div>
<div id="comment-61359-info" class="comment-info">
<span class="comment-age">(26 Dec '17, 02:11)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="61366"></span>
<div id="comment-61366" class="comment">
<div id="post-61366-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, no, actually not. I'm talking about those big office printers like for example <a href="http://inkless.ink/wp-content/uploads/2016/10/393322951-1.jpg">this one</a>. Those haven't been moved in years, often even have card readers attached to the wall (making it difficult to move them) and there's even a list of printers provided by the university. I'm just talking about a regular amenity, just like a photo booth or whatsoever.</p>
</div>
<div id="comment-61366-info" class="comment-info">
<span class="comment-age">(26 Dec '17, 13:15)</span> <span class="comment-user userinfo">nw520</span>
</div>
</div>
</div>
<div id="comment-tools-61351" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61351-form-container" class="comment-form-container">
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

<span id="61365"></span>

<div id="answer-container-61365" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61365-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61365-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61365-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks like a node tagged <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dprinter"><code>amenity=printer</code></a> is the best option at the moment. While far from established with less than 100 uses and no application support, it's been mentioned in the wiki since 2014‎, and the brief definition found in the wiki ("public printer") seems to point at the use case in question, rather than other possible meanings of the word "printer".</p>
<p>You may consider including other tags commonly found on indoor features, such as <code>level=*</code>. See <a href="https://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging">Simple Indoor Tagging</a> for a more detailed reference if desired.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Dec '17, 12:06</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Dec '17, 12:10</strong> </span></p>
</div>
</div>
<div id="comments-container-61365" class="comments-container">
<span id="61369"></span>
<div id="comment-61369" class="comment">
<div id="post-61369-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately "public printer" doesn't distinguish between the two possible cases (and yes, this is the problem with trying to map everything in the "amenity" space!).</p>
</div>
<div id="comment-61369-info" class="comment-info">
<span class="comment-age">(26 Dec '17, 13:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="61374"></span>
<div id="comment-61374" class="comment">
<div id="post-61374-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hm, there do indeed seem to be a considerable number of printer's shops tagged as <code>amenity=printer</code>. I would have expected to see those tagged as <code>shop=*</code>, <code>office=*</code> or possibly even <code>craft=*</code>. Is there any unambiguous term that could be used as the value?</p>
</div>
<div id="comment-61374-info" class="comment-info">
<span class="comment-age">(26 Dec '17, 16:07)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-61365" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61365-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61356"></span>

<div id="answer-container-61356" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61356-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61356-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61356-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If it is in a Uni building create a node with Tag:amenity=printer .Public Libraries usually have some printing facilities as well so i guess you could do a node for them as well. They may get rendered this one does, it's a business that i have found <a href="http://www.openstreetmap.org/node/2704917063#map=19/52.07690/4.35368">http://www.openstreetmap.org/node/2704917063#map=19/52.07690/4.35368</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Dec '17, 14:55</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Dec '17, 15:02</strong> </span></p>
</div>
</div>
<div id="comments-container-61356" class="comments-container">
<span id="61363"></span>
<div id="comment-61363" class="comment">
<div id="post-61363-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your suggestion. I guess I'll use amenity=printer. In the OSM Wiki there's only a shop=copyshop (like in your link) documentation but nothing mentioned about stand-alone printers or printing service included in other kind of shops and facilities.</p>
</div>
<div id="comment-61363-info" class="comment-info">
<span class="comment-age">(26 Dec '17, 11:52)</span> <span class="comment-user userinfo">nw520</span>
</div>
</div>
<span id="61364"></span>
<div id="comment-61364" class="comment">
<div id="post-61364-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"amenity=printer" is used in OSM for something else, so it's not a good choice. See <a href="https://www.openstreetmap.org/way/482115055">https://www.openstreetmap.org/way/482115055</a> for an example. A "printer" or "printer's" is somewhere that you go (a shop or office) to get something printed.</p>
<p>Example taginfo search: <a href="https://taginfo.openstreetmap.org/tags/amenity=printer">https://taginfo.openstreetmap.org/tags/amenity=printer</a> , <a href="https://overpass-turbo.eu/s/u1u">https://overpass-turbo.eu/s/u1u</a> in overpass.</p>
</div>
<div id="comment-61364-info" class="comment-info">
<span class="comment-age">(26 Dec '17, 11:58)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-61356" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61356-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61352"></span>

<div id="answer-container-61352" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61352-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61352-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-61352-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi nw520, since a printer is an movable object, it is like a moving bench in a park, dont tag it locally. Or ad public=printer to the building itself just to make clear there is one available.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Dec '17, 10:43</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-61352" class="comments-container">
<span id="61355"></span>
<div id="comment-61355" class="comment">
<div id="post-61355-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Printers are theoretically movable, but that should not preclude mapping them unless they're <em>actually</em> being moved regularly. A lot of the things we map – including traffic signs – could be moved within a couple minutes, but in practice they stick around for years or decades. The same is true for many public printers at universities.</p>
</div>
<div id="comment-61355-info" class="comment-info">
<span class="comment-age">(25 Dec '17, 12:54)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-61352" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61352-form-container" class="comment-form-container">
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

