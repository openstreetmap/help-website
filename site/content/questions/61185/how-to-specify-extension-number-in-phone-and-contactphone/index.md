+++
type = "question"
title = "How to specify extension number in `phone` and `contact:phone`?"
description = '''During my mapping journey, I have encountered several places which are perfectly notable as POI, but I have problem recording their phone contact information on OpenStreetMap as they made use of extension number; Wiki entry on phone and contact:phone key does not mention extension number at all. For...'''
date = "2017-12-14T13:53:00Z"
lastmod = "2021-04-23T22:12:00Z"
weight = 61185
keywords = [ "mobile", "phone", "contact", "dialer" ]
aliases = [ "/questions/61185" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to specify extension number in \`phone\` and \`contact:phone\`?](/questions/61185/how-to-specify-extension-number-in-phone-and-contactphone)

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
<span id="post-61185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61185-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-61185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>During my mapping journey, I have encountered several places which are perfectly notable as POI, but I have problem recording their phone contact information on OpenStreetMap <strong>as they made use of <a href="https://en.wikipedia.org/wiki/Extension_%28telephone%29">extension number</a></strong>; Wiki entry on <a href="https://wiki.openstreetmap.org/wiki/Key:phone?oldid=1534098"><em>phone</em></a> and <a href="https://wiki.openstreetmap.org/wiki/Key:contact?oldid=1513869"><em>contact:phone</em></a> key does not mention extension number at all.</p>
<p>For example: <a href="https://www.openstreetmap.org/node/5283277354#map=19/13.74675/100.53012">Art Library</a>, which is located inside <a href="https://www.openstreetmap.org/way/48966995#map=19/13.74674/100.53028">Bangkok Art and Culture Centre</a>, has following phone number:</p>
<pre><code>+66 2 214 6630 ext. 126</code></pre>
<p>Dialing <code>+66 2 214 6630</code> alone will lead you straight to Bangkok Art and Culture Centre's main PBX. While one can ask the operator to manually transfer the call, it is time-consuming and defeats the purpose of documening phone number on the library POI to begin with (it is equivalent to calling Bangkok Art and Culture Centre- the enclosing feature). On few other places I have visited and called, there are no human operator present at all; only voice message “This is (...), please dial an internal extension number” is played.</p>
<p>According to <a href="http://www.androidpolice.com/2010/05/10/how-to-add-hard-wait-and-soft-2-3-sec-pauses-to-your-android-contacts/">(1)</a> and <a href="https://www.imore.com/daily-tip-automatically-dialing-extension-iphone">(2)</a>, default dialer program in Android and iOS seems to support special “Pause” numbers in contact entries, which are used to separate main number from extension number:</p>
<ul>
<li><code>,</code> (comma) can be added to introduce ~3 sec pause before DTMF-dialing the rest of number.</li>
<li><code>;</code> (semicolon) can be added to show confirmation prompt (time-unspecifed pause) before DTMF-dialing the rest of number.</li>
</ul>
<p>As semicolon is used as OpenStreetMap's value separator, <code>p</code> and <code>w</code> can be used instead of <code>,</code> and <code>;</code> at least on Android dialer (not sure about iOS though), unless one is willing to use a less-readable <a href="https://wiki.openstreetmap.org/wiki/Semi-colon_value_separator?oldid=1439144#Escaping_with_.27.3B.3B.27">escape sequence</a>.</p>
<p>So, I would like to know...</p>
<ul>
<li><strong>Are there any proposal, concensus, or relevant standard document to look at, for ways to specify phone extension number on OpenStreetMap data attribute?</strong></li>
<li>Does mobile-based OpenStreetMap programs (e.g. <a href="https://en.wikipedia.org/wiki/OsmAnd">OsmAnd</a> and <a href="https://en.wikipedia.org/wiki/Maps.me">Maps.me</a>) react correctly to phone number written with these kinds of separator?</li>
<li>Does dialer on both Android and iOS dial them properly (with pause/prompt) when invoked from map programs?</li>
<li>Does <code>p</code> and <code>w</code> separator work correctly on iOS dialer when invoked from map programs?</li>
</ul>
<p>Side notes:</p>
<ul>
<li><a href="https://tools.ietf.org/html/rfc3966">RFC 3966</a> a.k.a. <code>tel:</code> protocol apparently allows specifying extension via <code>;ext=</code>, so the above number could be written as this <span>tel: link</span>: <code>tel:+6622146630;ext=126</code> (It still clashes with OpenStreetMap's semicolon separator, though)</li>
<li>Some feature phones allow <code>p</code> and <code>w</code> separators in contact entries as well (though not <code>,</code> and <code>;</code>).</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mobile" rel="tag" title="see questions tagged &#39;mobile&#39;">mobile</span> <span class="post-tag tag-link-phone" rel="tag" title="see questions tagged &#39;phone&#39;">phone</span> <span class="post-tag tag-link-contact" rel="tag" title="see questions tagged &#39;contact&#39;">contact</span> <span class="post-tag tag-link-dialer" rel="tag" title="see questions tagged &#39;dialer&#39;">dialer</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Dec '17, 13:53</strong></p>
<img src="https://secure.gravatar.com/avatar/d0bf78fa6f7ca788533635c1bb605e12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nutchanon%20Wetchasit&#39;s gravatar image" />
<p><span>Nutchanon We...</span><br />
<span class="score" title="290 reputation points">290</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nutchanon Wetchasit has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jan '18, 04:34</strong> </span></p>
</div>
</div>
<div id="comments-container-61185" class="comments-container">
&#10;</div>
<div id="comment-tools-61185" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61185-form-container" class="comment-form-container">
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

<span id="67653"></span>

<div id="answer-container-67653" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67653-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Note that according to Overpass query on OpenStreetMap data at the time of this writing (21-Jan-2019)...</p>
<ul>
<li><a href="https://overpass-turbo.eu/?Q=node%5B%7E%22%5E%28contact%3A%29%3Fphone%28%3A.%2B%29%3F%24%22%7E%22%5B0-9%5D%5B-+%5D*p%5B-+%5D*%5B0-9%5D%22%5D%3Bout%3B%28way%5B%7E%22%5E%28contact%3A%29%3Fphone%28%3A.%2B%29%3F%24%22%7E%22%5B0-9%5D%5B-+%5D*p%5B-+%5D*%5B0-9%5D%22%5D%3Brelation%5B%7E%22%5E%28contact%3A%29%3Fphone%28%3A.%2B%29%3F%24%22%7E%22%5B0-9%5D%5B-+%5D*p%5B-+%5D*%5B0-9%5D%22%5D%3B%29-%3E._%3Bout%3B%3E%3Bout+skel%3B&amp;R"><code>p</code> separator seems to be used sparsely</a>, though <strong>all of them are apparently used for extension number</strong>.</li>
<li><a href="https://overpass-turbo.eu/?Q=node%5B~%22%5E%28contact%3A%29%3Fphone%28%3A.%2B%29%3F%24%22~%22%5B0-9%5D%5B-+%5D*w%5B-+%5D*%5B0-9%5D%22%5D%3Bout%3B%28way%5B~%22%5E%28contact%3A%29%3Fphone%28%3A.%2B%29%3F%24%22~%22%5B0-9%5D%5B-+%5D*w%5B-+%5D*%5B0-9%5D%22%5D%3Brelation%5B~%22%5E%28contact%3A%29%3Fphone%28%3A.%2B%29%3F%24%22~%22%5B0-9%5D%5B-+%5D*w%5B-+%5D*%5B0-9%5D%22%5D%3B%29-%3E._%3Bout%3B%3E%3Bout+skel%3B&amp;R"><code>w</code> separator is not used at all.</a></li>
<li><a href="https://overpass-turbo.eu/?Q=node%5B%7E%22%5E%28contact%3A%29%3Fphone%28%3A.%2B%29%3F%24%22%7E%22%5B0-9%5D%5B-+%5D*%2C%5B-+%5D*%5B0-9%5D%22%5D%3Bout%3B%28way%5B%7E%22%5E%28contact%3A%29%3Fphone%28%3A.%2B%29%3F%24%22%7E%22%5B0-9%5D%5B-+%5D*%2C%5B-+%5D*%5B0-9%5D%22%5D%3Brelation%5B%7E%22%5E%28contact%3A%29%3Fphone%28%3A.%2B%29%3F%24%22%7E%22%5B0-9%5D%5B-+%5D*%2C%5B-+%5D*%5B0-9%5D%22%5D%3B%29-%3E._%3Bout%3B%3E%3Bout+skel%3B&amp;R"><code>,</code> separator seems to be used ubiquitously</a>; but most of them are apparently used as <strong>poor substitute of <a href="https://wiki.openstreetmap.org/wiki/Semi-colon_value_separator">semicolon value separator</a>, not for extenstion number</strong>.</li>
<li><a href="https://overpass-turbo.eu/?Q=node%5B%7E%22%5E%28contact%3A%29%3Fphone%28%3A.%2B%29%3F%24%22%7E%22%5B0-9%5D%5B-+%5D*%3B%3B%5B-+%5D*%5B0-9%5D%22%5D%3Bout%3B%28way%5B%7E%22%5E%28contact%3A%29%3Fphone%28%3A.%2B%29%3F%24%22%7E%22%5B0-9%5D%5B-+%5D*%3B%3B%5B-+%5D*%5B0-9%5D%22%5D%3Brelation%5B%7E%22%5E%28contact%3A%29%3Fphone%28%3A.%2B%29%3F%24%22%7E%22%5B0-9%5D%5B-+%5D*%3B%3B%5B-+%5D*%5B0-9%5D%22%5D%3B%29-%3E._%3Bout%3B%3E%3Bout+skel%3B&amp;R"><code>;;</code> separator is not used at all.</a></li>
</ul>
<p>So, at the moment, if one is going to record phone extension number on OpenStreetMap with <em>minimal ambiguity</em>, then <code>p</code> or <code>w</code> separator should be used.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '19, 04:26</strong></p>
<img src="https://secure.gravatar.com/avatar/d0bf78fa6f7ca788533635c1bb605e12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nutchanon%20Wetchasit&#39;s gravatar image" />
<p><span>Nutchanon We...</span><br />
<span class="score" title="290 reputation points">290</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nutchanon Wetchasit has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-67653" class="comments-container">
<span id="79829"></span>
<div id="comment-79829" class="comment">
<div id="post-79829-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>2021 update: I wrote about the situation between <code>phone=</code> and <code>contact:phone=</code> on wiki in <a href="https://wiki.openstreetmap.org/wiki/Talk:Key:contact#Internal_phone_extension_number">https://wiki.openstreetmap.org/wiki/Talk:Key:contact#Internal_phone_extension_number</a> , as prompted by <a href="https://wiki.openstreetmap.org/wiki/Talk:Key:phone#Extension_numbers">https://wiki.openstreetmap.org/wiki/Talk:Key:phone#Extension_numbers</a> and a Discord question.</p>
</div>
<div id="comment-79829-info" class="comment-info">
<span class="comment-age">(23 Apr '21, 22:12)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-67653" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67653-form-container" class="comment-form-container">
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

