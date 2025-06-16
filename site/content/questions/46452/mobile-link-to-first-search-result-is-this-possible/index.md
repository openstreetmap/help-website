+++
type = "question"
title = "Mobile link to first search result - is this possible?"
description = '''How can I create a link to a mobile friendly OSM site, based on arbitrary input? For example, a Twitter user&#x27;s location may be 34.63677866,135.22868514 or Oxford, UK or Düsseldorf. I don&#x27;t have any control over the format of text they input. That works fine with Nominatim (https://nominatim.openstre...'''
date = "2015-11-07T23:45:00Z"
lastmod = "2015-11-09T18:38:00Z"
weight = 46452
keywords = [ "mobile", "url", "link", "osm.org" ]
aliases = [ "/questions/46452" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mobile link to first search result - is this possible?](/questions/46452/mobile-link-to-first-search-result-is-this-possible)

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
<span id="post-46452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46452-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I create a link to a mobile friendly OSM site, based on arbitrary input?</p>
<p>For example, a Twitter user's location may be <code>34.63677866,135.22868514</code> or <code>Oxford, UK</code> or <code>Düsseldorf</code>. I don't have any control over the format of text they input.</p>
<p>That works fine with Nominatim (<a href="https://nominatim.openstreetmap.org/search?q=Whatever"><code>https://nominatim.openstreetmap.org/search?q=Whatever</code></a>), but the results are not mobile friendly.</p>
<p><img src="https://cloud.githubusercontent.com/assets/837136/11017819/4c1b5d70-85a4-11e5-865b-83f134811ac9.jpg" alt="alt text" /></p>
<p>The regular OSM <em>is</em> mobile friendly, but I can't seem to find the syntax which will allow me to link directly to a search result.</p>
<p>For example, <span>the documentation shows how to link to a Lat/Long</span>, but not a search result.</p>
<p>Ideally, I want to write something like:</p>
<pre><code>https://www.openstreetmap.org/?q=34.63677866,135.22868514
https://www.openstreetmap.org/?q=Oxford,UK
https://www.openstreetmap.org/?q=D%C3%BCsseldorf</code></pre>
<p>I appreciate that there may be ambiguous results returned for search queries - but the first result is usually the best.</p>
<p>Currently, the best I can do is <a href="https://www.openstreetmap.org/search?query=oxford%2CUK"><code>https://www.openstreetmap.org/search?query=oxford%2CUK</code></a> - but that takes me to a list of results:</p>
<p><img src="/upfiles/14469437085940.jpg" alt="osm.org search results screenshot on mobile device" /></p>
<p>So, how do I link to the first result of a search in a mobile friendly manner?</p>
<p>Thanks :-)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mobile" rel="tag" title="see questions tagged &#39;mobile&#39;">mobile</span> <span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-link" rel="tag" title="see questions tagged &#39;link&#39;">link</span> <span class="post-tag tag-link-osm.org" rel="tag" title="see questions tagged &#39;osm.org&#39;">osm.org</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Nov '15, 23:45</strong></p>
<img src="https://secure.gravatar.com/avatar/52cb49a66755f31abf4df9a6549f0f9c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terence%20Eden&#39;s gravatar image" />
<p><span>Terence Eden</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terence Eden has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Nov '15, 01:19</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</img>
</div>
</div>
<div id="comments-container-46452" class="comments-container">
<span id="46454"></span>
<div id="comment-46454" class="comment">
<div id="post-46454-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That doesn't take me to the first result. It takes me to a list of results. I want the user click on a link and see a map. I've updated the question to reflect that. Thanks.</p>
</div>
<div id="comment-46454-info" class="comment-info">
<span class="comment-age">(08 Nov '15, 00:52)</span> <span class="comment-user userinfo">Terence Eden</span>
</div>
</div>
<span id="46455"></span>
<div id="comment-46455" class="comment">
<div id="post-46455-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>thanks for the clarification (my old text - since the conversion technique does not work currently: Umm, do I miss something or are you just searching for this kind of URL? <a href="https://www.openstreetmap.org/search?query=oxford%2CUK">https://www.openstreetmap.org/search?query=oxford%2CUK</a> (you get there just by using the search box on osm.org))</p>
</div>
<div id="comment-46455-info" class="comment-info">
<span class="comment-age">(08 Nov '15, 01:16)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="46456"></span>
<div id="comment-46456" class="comment">
<div id="post-46456-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can't add a own custom service on server side, can't you?</p>
</div>
<div id="comment-46456-info" class="comment-info">
<span class="comment-age">(08 Nov '15, 07:38)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="46458"></span>
<div id="comment-46458" class="comment">
<div id="post-46458-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/4984/iii">@iii</a> I'm not sure quite what you mean. I don't want to install an entire OSM instance for this. I just want to point people at a map. Doesn't have to be the main OSM site - I'd use Open MapQuest but they don't support mobile.</p>
</div>
<div id="comment-46458-info" class="comment-info">
<span class="comment-age">(08 Nov '15, 11:20)</span> <span class="comment-user userinfo">Terence Eden</span>
</div>
</div>
<span id="46461"></span>
<div id="comment-46461" class="comment">
<div id="post-46461-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you explain what you are actually trying to do?</p>
<p>You say you want to "create a link" but "in what"? If the answer to that is "in some website code" then you'd do exactly what SimonPoole describes below below in that website code. If the answer is "in something on a mobile phone" then you'd probably create a web app on the phones (using something like Cordova/Phonegap) and add the logic there. It's easier to do that it sounds - I helped someone with no JavaScript experience at all do this a couple of years ago and they figured out the Nominatim part for themselves.</p>
</div>
<div id="comment-46461-info" class="comment-info">
<span class="comment-age">(08 Nov '15, 15:58)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="46462"></span>
<div id="comment-46462" class="comment not_top_scorer">
<div id="post-46462-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@someoneelse</a> On Twitter, people can set their location - either in their Bio or in a tweet. I am generating a link on a web page to that location, for example, <a href="https://maps.google.com/maps?q=Oxford">https://maps.google.com/maps?q=Oxford</a> or <a href="https://maps.google.com/maps?q=34.63677866,135.22868514">https://maps.google.com/maps?q=34.63677866,135.22868514</a> ... That takes a user to a website (suitable for mobile &amp; desktop) which has the "best guess" prominently displayed. Not a list of suggestion - just a map.</p>
</div>
<div id="comment-46462-info" class="comment-info">
<span class="comment-age">(08 Nov '15, 16:12)</span> <span class="comment-user userinfo">Terence Eden</span>
</div>
</div>
<span id="46463"></span>
<div id="comment-46463" class="comment not_top_scorer">
<div id="post-46463-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... so on the web page where you're generating the link, you'd add code that does what SimonPoole suggests, and generate the link based on that.</p>
</div>
<div id="comment-46463-info" class="comment-info">
<span class="comment-age">(08 Nov '15, 16:18)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46452" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-46452-form-container" class="comment-form-container">
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

<span id="46460"></span>

<div id="answer-container-46460" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46460-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-46460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>IMHO you are approaching this the wrong way. What you need to do is query nominatim directly (or any other search engine)</p>
<ul>
<li><p>get list of results</p></li>
<li><p>take first one</p></li>
<li><p>and generate either a link with the position or the object in question</p></li>
</ul>
<p>You won't be able to do the above using the openstreetmap.org website as a "proxy" to nominatim, at least not without support in the actuall rails port code.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Nov '15, 15:45</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Nov '15, 15:46</strong> </span></p>
</div>
</div>
<div id="comments-container-46460" class="comments-container">
<span id="46464"></span>
<div id="comment-46464" class="comment">
<div id="post-46464-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As I said in a different comment, I've got a long list of locations. Sending ~200 queries is a bit of an unnecessary overhead.</p>
<p>On a service like Google, I don't need to make an API query, I can just craft a URL and, if the user chooses to click on it, they get taken to a map.</p>
<ul>
<li><a href="https://maps.google.com/maps?q=Oxford">https://maps.google.com/maps?q=Oxford</a></li>
<li><a href="https://maps.google.com/maps?q=34.63677866,135.22868514">https://maps.google.com/maps?q=34.63677866,135.22868514</a></li>
<li><a href="https://maps.google.com/maps?q=Pizza">https://maps.google.com/maps?q=Pizza</a></li>
</ul>
<p>The nominatim service does this perfectly, but isn't mobile friendly:</p>
<ul>
<li><a href="https://nominatim.openstreetmap.org/search?q=Oxford">https://nominatim.openstreetmap.org/search?q=Oxford</a></li>
<li><a href="https://nominatim.openstreetmap.org/search?q=34.63677866,135.22868514">https://nominatim.openstreetmap.org/search?q=34.63677866,135.22868514</a></li>
<li><a href="https://nominatim.openstreetmap.org/search?q=Pizza">https://nominatim.openstreetmap.org/search?q=Pizza</a></li>
</ul>
<p>Same as Open MapQuest:</p>
<ul>
<li><a href="http://open.mapquest.com/?q=oxford">http://open.mapquest.com/?q=oxford</a></li>
</ul>
<p>Takes me to the right map, but not mobile friendly.</p>
<p>All I want is an OSM site which is mobile friendly and will take the user to a "best guess" based on a query.</p>
</div>
<div id="comment-46464-info" class="comment-info">
<span class="comment-age">(08 Nov '15, 16:22)</span> <span class="comment-user userinfo">Terence Eden</span>
</div>
</div>
<span id="46466"></span>
<div id="comment-46466" class="comment">
<div id="post-46466-score" class="comment-score">
3
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/9471/terence-eden"></a><a href="https://help.openstreetmap.org/users/9471/terence-eden">@Terence Eden</a> there is nothing stoping you from producing such a site. Doable with some JS and one of the JS map display libraries in a jiffy.</p>
<p>But I guess that is not the real issue, which seems to be a misunderstanding of the nature of the OpenStreetMap web site and associated service. They a mainly geared towards mapping support and support for any other usage is at best incidential (this has been a matter of debate since early on in OSM history, but it is in any case the current situation). The tl;dr version is that OSM is about collecting and distributiong a open and freely available geo-dataset, -not- about providing free services. Given that you can simply take the data and build your own, this should not be a big issue.</p>
</div>
<div id="comment-46466-info" class="comment-info">
<span class="comment-age">(08 Nov '15, 16:56)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="46481"></span>
<div id="comment-46481" class="comment">
<div id="post-46481-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... and, Terence, you should have a closer look to the wiki page <a href="https://wiki.openstreetmap.org/wiki/Search_engines">https://wiki.openstreetmap.org/wiki/Search_engines</a> just to find other nominatim based search engines, or even very own standing search engines based on raw OSM data.</p>
</div>
<div id="comment-46481-info" class="comment-info">
<span class="comment-age">(09 Nov '15, 18:38)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-46460" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46460-form-container" class="comment-form-container">
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

