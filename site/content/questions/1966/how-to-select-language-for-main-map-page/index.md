+++
type = "question"
title = "How to select language for main map page?"
description = '''I&#x27;m probably missing something simple, but I can&#x27;t find any way to make the main OSM map page appear in another language, e.g. Spanish. I mean show &quot;ayuda&quot; and &quot;buscar&quot; in the menu instead of &quot;help&quot; and &quot;search&quot;, etc. I&#x27;ve tried setting browser preferences, and searching the web for help, but no joy...'''
date = "2010-12-31T16:41:00Z"
lastmod = "2022-03-15T17:50:00Z"
weight = 1966
keywords = [ "internationalization", "osm.org", "language" ]
aliases = [ "/questions/1966" ]
osqa_answers = 7
osqa_accepted = false
+++

<div class="headNormal">

# [How to select language for main map page?](/questions/1966/how-to-select-language-for-main-map-page)

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
<span id="post-1966-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1966-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-1966-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm probably missing something simple, but I can't find any way to make the main OSM map page appear in another language, e.g. Spanish. I mean show "ayuda" and "buscar" in the menu instead of "help" and "search", etc. I've tried setting browser preferences, and searching the web for help, but no joy. Can anybody help? Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-internationalization" rel="tag" title="see questions tagged &#39;internationalization&#39;">internationalization</span> <span class="post-tag tag-link-osm.org" rel="tag" title="see questions tagged &#39;osm.org&#39;">osm.org</span> <span class="post-tag tag-link-language" rel="tag" title="see questions tagged &#39;language&#39;">language</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Dec '10, 16:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a8992ad9a83eacdd6388ed265d3f6921?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tongro&#39;s gravatar image" />
<p><span>tongro</span><br />
<span class="score" title="701 reputation points">701</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tongro has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Mar '14, 20:36</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-1966" class="comments-container">
&#10;</div>
<div id="comment-tools-1966" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1966-form-container" class="comment-form-container">
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

7 Answers:

</div>

</div>

<span id="1977"></span>

<div id="answer-container-1977" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1977-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-1977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I seem to have it figured out now. It seems regional varieties of Spanish are not recognised, and the English default page is returned instead. When the client sends the HTTP header "Accept-Language: es-es" an English page is returned, but "es-es,es" or "es" gets a Spanish page. It would surely make more sense to default to the base language "es" if the regional "es-*" is not recognised? Anyway it sort of works now.</p>
<p>Thanks a lot.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jan '11, 12:57</strong></p>
<img src="https://secure.gravatar.com/avatar/a8992ad9a83eacdd6388ed265d3f6921?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tongro&#39;s gravatar image" />
<p><span>tongro</span><br />
<span class="score" title="701 reputation points">701</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tongro has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jan '11, 13:16</strong> </span></p>
</div>
</div>
<div id="comments-container-1977" class="comments-container">
<span id="2235"></span>
<div id="comment-2235" class="comment">
<div id="post-2235-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Actually, the behavior you describe is correct, and is even specifically noted in RFC 2616 (see the last paragraph of <a href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4">http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4</a>), mentioning “A user agent might suggest in such a case to add [the base language] to get the best matching behavior.”</p>
</div>
<div id="comment-2235-info" class="comment-info">
<span class="comment-age">(16 Jan '11, 21:52)</span> <span class="comment-user userinfo">Mormegil</span>
</div>
</div>
<span id="5936"></span>
<div id="comment-5936" class="comment">
<div id="post-5936-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yet is there a way to incorporate in the address to the website a language specification? I am thinking of something like <a href="https://www.openstreetmap.org/?lang=es">https://www.openstreetmap.org/?lang=es</a> or so. Thanks a lot.</p>
</div>
<div id="comment-5936-info" class="comment-info">
<span class="comment-age">(21 Jun '11, 21:53)</span> <span class="comment-user userinfo">GastonJumoke</span>
</div>
</div>
</div>
<div id="comment-tools-1977" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1977-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1969"></span>

<div id="answer-container-1969" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1969-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-1969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Go to <a href="http://openstreetmap.org">openstreetmap.org</a>, and login to your account. Then click on your user name, in the top right corner, which will take you to your user page. Then click on the link for "My settings".</p>
<p>Part way down that page, there is a box for "Preferred Languages:". So you can enter the codes for the languages you would prefer. For Spanish, just enter <code>es</code>. Then click the button for "Save changes", then the OSM page should be in Spanish (whenever you are logged in).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Dec '10, 18:43</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-1969" class="comments-container">
<span id="1971"></span>
<div id="comment-1971" class="comment">
<div id="post-1971-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>OK, thanks. However, what I'm looking for is to have the page appearing in Spanish every time for anybody who clicks on a link I supply, or at least for anybody whose browser's locale is set to Spanish. I'm developing a website for Spanish speakers, which contains a link to OSM, and I don't want to be forcing English on them.</p>
</div>
<div id="comment-1971-info" class="comment-info">
<span class="comment-age">(31 Dec '10, 19:52)</span> <span class="comment-user userinfo">tongro</span>
</div>
</div>
<span id="1972"></span>
<div id="comment-1972" class="comment">
<div id="post-1972-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just testing this now:</p>
<p>Using Chromium, changing the accept language in the browser, does change the language on <a href="http://osm.org">osm.org</a> (if logged out). So all of the page is in Spanish/German etc. But using Firefox, changing the language doesn't make any difference - its all still in English.</p>
<p>I don't know if this is something specific to my setup, or something about Firefox? I have tried clearing all cookies, it doesn't make any difference.</p>
<p>I don't know what browsers you've tried, and what happens with each? Probably worth asking about this on the mailing list, or reporting it on Trac.</p>
</div>
<div id="comment-1972-info" class="comment-info">
<span class="comment-age">(31 Dec '10, 21:50)</span> <span class="comment-user userinfo">Vclaw</span>
</div>
</div>
</div>
<div id="comment-tools-1969" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1969-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52771"></span>

<div id="answer-container-52771" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52771-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52771-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52771-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Many years gone but nothing changed, as far as I can see? So I'd like to ask again - where do we find the setting for the map's language? I don't understand the texts in this thread but I see that still the maps language selection is hidden (or missing??). As the T.O. I'm not asking about settings for registered users or settings for any web site texts, we are talking about the map itself, when any www user from any country takes a look at the map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '16, 11:46</strong></p>
<img src="https://secure.gravatar.com/avatar/caf2da085699130e814702106a4df56a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="micmen&#39;s gravatar image" />
<p><span>micmen</span><br />
<span class="score" title="54 reputation points">54</span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="micmen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52771" class="comments-container">
<span id="52772"></span>
<div id="comment-52772" class="comment">
<div id="post-52772-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>The default map at OpenStreetMap displays whatever is in the 'name' tag for each object, which is usually the local name. So places in England are shown in English, places in France get their French name, and so on. There is no option to change this on osm.org - the technology currently used to draw the maps doesn't make it practical.</p>
</div>
<div id="comment-52772-info" class="comment-info">
<span class="comment-age">(01 Nov '16, 13:16)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="52773"></span>
<div id="comment-52773" class="comment">
<div id="post-52773-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sounds like a really bad idea? Ich had a look at an area in middle east and everything was in any eastern letters, I couldn't even see, what countries that were... Doesn't make sense?? OSM programmers thought, that every user all over the world will only look at maps around the own home country?? That's a mistake, they definately will NOT...</p>
</div>
<div id="comment-52773-info" class="comment-info">
<span class="comment-age">(01 Nov '16, 14:42)</span> <span class="comment-user userinfo">micmen</span>
</div>
</div>
<span id="52774"></span>
<div id="comment-52774" class="comment">
<div id="post-52774-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The "Standard" rendering at openstreetmap.org is intended for the use of mappers to check their work, which will generally be in their native language. It's only one of many different renderings, so I'm sure there's another one out there that can be set to render in specific languages. Anyway, the original question was about the language of the website itself, not the rendered tiles.</p>
</div>
<div id="comment-52774-info" class="comment-info">
<span class="comment-age">(01 Nov '16, 15:58)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="83863"></span>
<div id="comment-83863" class="comment">
<div id="post-83863-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe the middle east is different, but I never undestood why people wanted to have an english map when I lived in Russia in 2001/02. Street names were all in cyrillic and comparing patterns is possible even for 2year old children. So it makes sense to offer the map in the local language by default.</p>
</div>
<div id="comment-83863-info" class="comment-info">
<span class="comment-age">(15 Mar '22, 17:50)</span> <span class="comment-user userinfo">Keinstein</span>
</div>
</div>
</div>
<div id="comment-tools-52771" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52771-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78129"></span>

<div id="answer-container-78129" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78129-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78129-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78129-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It turns our the content is not multi-language. The servers have only one set of tiles and they use the default language in the OSM database. To have the content in a different language you will have to use a rendering engine that have it in your language. Some mobile apps like OSMand I think support multiple languages. There are many rendering engines for OSM. But the openstreetmap.org site itself does not do that. So as you saw when you change the language in the web page, only the interface changes. The tiles are statif. They simply do not compute multiple tile sets. The mapping pages of Google and Apple amont other, have moved to a vector based rendering years ago. In such a system text is text and it is easy to flip language. But with a tile-based engine the text is built into the tiles as pixels and it it is not possible without computing a completely separate set of tiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '20, 14:38</strong></p>
<img src="https://secure.gravatar.com/avatar/bdeac300a7cbecaa3963849aa08bcb18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Martin%20Chalifoux&#39;s gravatar image" />
<p><span>Martin Chali...</span><br />
<span class="score" title="39 reputation points">39</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Martin Chalifoux has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78129" class="comments-container">
<span id="78130"></span>
<div id="comment-78130" class="comment">
<div id="post-78130-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>.. and if you do want a different language of a classic openstreetmap-carto like raster map (or close to that), check out the sites of local chapters like e.g. <a href="https://www.openstreetmap.fr">https://www.openstreetmap.fr</a>, that publishes a map in french as well as in breton (often only for a region, but some also worldwide) or check out my project at <a href="https://www.osmap.info">https://www.osmap.info</a> where you'll find ten different language versions of the world map.</p>
</div>
<div id="comment-78130-info" class="comment-info">
<span class="comment-age">(30 Dec '20, 14:47)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="78157"></span>
<div id="comment-78157" class="comment">
<div id="post-78157-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Guys, the original question is specifically on the language displayed on the web site. If you want to discuss the language of the map labels please start a new question.</p>
</div>
<div id="comment-78157-info" class="comment-info">
<span class="comment-age">(31 Dec '20, 13:31)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="78159"></span>
<div id="comment-78159" class="comment">
<div id="post-78159-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I see. You will I think understand that it is not obvious that the language of the map is a different question to the language of the website containing the map. But this is clear now.</p>
</div>
<div id="comment-78159-info" class="comment-info">
<span class="comment-age">(31 Dec '20, 13:36)</span> <span class="comment-user userinfo">Jim Killock</span>
</div>
</div>
</div>
<div id="comment-tools-78129" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78129-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67199"></span>

<div id="answer-container-67199" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67199-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-67199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the core issue here is that openstreetmap.org is a tile based rendering engine, not vector based. The engine generates one set of tiles using the default language. The text you see is part of the tiles, in the bitmap. It is not a text+fond as you may think it is. Generating many languages would require many sets of tiles (bitmaps), costly and not practical. Other map engines such as Google and Apple has moved to a vector based engine and this sort of stuff is much better handled. But this is a whole different technology to implement.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Dec '18, 17:25</strong></p>
<img src="https://secure.gravatar.com/avatar/bdeac300a7cbecaa3963849aa08bcb18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Martin%20Chalifoux&#39;s gravatar image" />
<p><span>Martin Chali...</span><br />
<span class="score" title="39 reputation points">39</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Martin Chalifoux has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67199" class="comments-container">
&#10;</div>
<div id="comment-tools-67199" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67199-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71662"></span>

<div id="answer-container-71662" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71662-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-71662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What a.. I'm in Thailand in'm a foreigner here. I really need a map. And I can't read ANY caption on openstreetmap. I'm here for 1 week only, sorry I can't learn local language that fast.</p>
<p>Englist mtf! Do you speak it???</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '19, 03:11</strong></p>
<img src="https://secure.gravatar.com/avatar/142bcc9f7c9832792ad49544118f21db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yoreck&#39;s gravatar image" />
<p><span>yoreck</span><br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yoreck has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71662" class="comments-container">
<span id="71670"></span>
<div id="comment-71670" class="comment">
<div id="post-71670-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi yoreck, first of all - some netiquette would be nice.</p>
<p>Openstreetmaps thailand map serves the about 70 million people of Thailand and is therefor rendered in their local language.</p>
<p>If you do need a map of thailand with english labels try a different layer on openstreetmap.org (cycle or transport have some english labels) or try <a href="https://www.osmap.asia/#5/10.898/99.976">this one</a> where you get english labels if they are present in openstreetmap data or otherwise transliterated thai labels.</p>
</div>
<div id="comment-71670-info" class="comment-info">
<span class="comment-age">(16 Nov '19, 13:55)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-71662" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71662-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78126"></span>

<div id="answer-container-78126" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78126-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-78126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><img src="/upfiles/Screenshot_2020-12-30_at_13.38.16.png" alt="Welsh not appearing on map" /></p>
<p>Hi, I am having problems with this. I have set the language in both browser to "cy" and personal preferences to "cy-gb, cy". This changes the interface language, but for me, as you can see on the streenshot I am getting English-language content despite the map data / Wikidata names being pretty well translated.</p>
<p>It strikes me that the map should default to the browser preference language, as well as the user preference, so any ideas why this is happening would be appreciated.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '20, 13:40</strong></p>
<img src="https://secure.gravatar.com/avatar/afaec6c1418f1eb4c64b0aafc9b58073?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Killock&#39;s gravatar image" />
<p><span>Jim Killock</span><br />
<span class="score" title="58 reputation points">58</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Killock has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Dec '20, 13:42</strong> </span></p>
</div>
</div>
<div id="comments-container-78126" class="comments-container">
<span id="78128"></span>
<div id="comment-78128" class="comment">
<div id="post-78128-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The map you see is built out of raster tiles - pngs with the local language applied from the name tag. Therefor the language on the map can't change at osm.org. A map version in cy can be found at <a href="https://www.openstreetmap.cymru">https://www.openstreetmap.cymru</a> .</p>
</div>
<div id="comment-78128-info" class="comment-info">
<span class="comment-age">(30 Dec '20, 14:35)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="78133"></span>
<div id="comment-78133" class="comment">
<div id="post-78133-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, shame the site is rather slow and just Wales, but thank you all the same.</p>
</div>
<div id="comment-78133-info" class="comment-info">
<span class="comment-age">(30 Dec '20, 17:04)</span> <span class="comment-user userinfo">Jim Killock</span>
</div>
</div>
<span id="78158"></span>
<div id="comment-78158" class="comment">
<div id="post-78158-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Guys, the original question is specifically on the language displayed on the web site. If you want to discuss the language of the map labels please start a new question.</p>
</div>
<div id="comment-78158-info" class="comment-info">
<span class="comment-age">(31 Dec '20, 13:31)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-78126" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78126-form-container" class="comment-form-container">
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

