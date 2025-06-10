+++
type = "question"
title = "What is the correct tag for English addresses in non-English speaking countries?"
description = '''Names are very clear, there is &quot;name&quot;, and &quot;name:en&quot; for the English version. But what about addresses? It&#x27;s important when searching for the English version of an address that it returns the same result as a search in the local language. So for example, in Mongolia a given address might be in the c...'''
date = "2014-05-11T03:40:00Z"
lastmod = "2014-05-13T04:39:00Z"
weight = 33069
keywords = [ "internationalization", "tagging", "address" ]
aliases = [ "/questions/33069" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What is the correct tag for English addresses in non-English speaking countries?](/questions/33069/what-is-the-correct-tag-for-english-addresses-in-non-english-speaking-countries)

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
<span id="post-33069-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33069-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33069-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Names are very clear, there is "name", and "name:en" for the English version. But what about addresses? It's important when searching for the English version of an address that it returns the same result as a search in the local language.</p>
<p>So for example, in Mongolia a given address might be in the city of улаанбаатар/Ulaanbaatar. Is it appropriate to use: addr:city=улаанбаатар and addr:city:en=Ulaanbaatar or is there some other format that should be used?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-internationalization" rel="tag" title="see questions tagged &#39;internationalization&#39;">internationalization</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 May '14, 03:40</strong></p>
<img src="https://secure.gravatar.com/avatar/c609fb48ca59d11e70826eb418be93d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SverreG&#39;s gravatar image" />
<p><span>SverreG</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SverreG has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 May '14, 11:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-33069" class="comments-container">
<span id="33071"></span>
<div id="comment-33071" class="comment">
<div id="post-33071-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm not that experienced with multilang approaches and <a href="http://wiki.openstreetmap.org/wiki/Internationalization">data internationalization</a>, but IMHO due to the heavy redundance (city name in every address within the city) and so a bad to maintain dataset, it's wise just to translate the name of the city at it's place node / boundary relation. Then it's up to the tools to be clever enough to understand this alternative name, too and we avoid heavy inconsistence because there is one in 10.000 Address nodes that has a wrong EN name :)</p>
</div>
<div id="comment-33071-info" class="comment-info">
<span class="comment-age">(11 May '14, 08:37)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="33093"></span>
<div id="comment-33093" class="comment">
<div id="post-33093-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So for example, talking about <a href="https://www.openstreetmap.org/node/2321491014">https://www.openstreetmap.org/node/2321491014</a></p>
<p>Currently searching for Zochin, "Залуучуудын өргөн чөлөө, улаанбаатар" returns the correct result, but searching for "Zochin, Youth Avenue, Ulaanbaatar" returns no results.</p>
<p>Is there anything I (as an English speaking OSM contributor who happens to be in Mongolia at the moment) can do to fix this problem?</p>
</div>
<div id="comment-33093-info" class="comment-info">
<span class="comment-age">(12 May '14, 06:50)</span> <span class="comment-user userinfo">SverreG</span>
</div>
</div>
<span id="33106"></span>
<div id="comment-33106" class="comment">
<div id="post-33106-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@SverreG</span> Write a front-end for Nominatim that translates "Youth Avenue, Ulaanbaatar" to "Залуучуудын өргөн чөлөө, улаанбаатар" perhaps? It might be worth talking to people who've done work in and around Nominatim what they currently do or plan to in this area. Perhaps on #osm-dev on IRC on the dev mailing list?</p>
</div>
<div id="comment-33106-info" class="comment-info">
<span class="comment-age">(12 May '14, 11:28)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33069" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33069-form-container" class="comment-form-container">
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

<span id="33116"></span>

<div id="answer-container-33116" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33116-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-33116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SverreG has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Localized names should always be put on the road, place or boundary, they refer to. The search engine can take it from there. What happens in Nominatim is that the <code>addr:*</code> tag is used only as a link to find the appropriate road or place object that make up the address. Once all objects are found, it builds the final display address from the name tags of these objects, localized as necessary.</p>
<p>So, in the case of "Залуучуудын өргөн чөлөө", it would be enough to add <code>name:en=Youth Avenue</code> to <a href="http://www.openstreetmap.org/way/81528745">this street</a>. A word of warning about translations though: Localized name tags like <code>name:en</code> should be added only, if such a translation is in common use, e.g. by local people or by foreign visitors. That is rarely the case for street names unless the country has more than one official language. If "Youth Avenue" is just a word-by-word translation of the Mongolian name that nobody ever uses, it shouldn't be included in OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 May '14, 16:28</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-33116" class="comments-container">
<span id="33128"></span>
<div id="comment-33128" class="comment">
<div id="post-33128-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you for the advice. I am currently working in an office near that street, and my Mongolian coworkers advise me that it is, in English, called both Youth Avenue (Залуучуудын өргөн чөлөө) but is also often referred to as Sambuu Street (Самбуугийн гудамж) which is what Google Maps shows it as. I've added a name:en tag, an alt_name tag, and an alt_name:en tag to the street.</p>
<p>I will try searching once indexes have had a chance to update and let you know.</p>
</div>
<div id="comment-33128-info" class="comment-info">
<span class="comment-age">(13 May '14, 04:39)</span> <span class="comment-user userinfo">SverreG</span>
</div>
</div>
</div>
<div id="comment-tools-33116" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33116-form-container" class="comment-form-container">
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

