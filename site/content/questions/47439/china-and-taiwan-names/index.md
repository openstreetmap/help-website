+++
type = "question"
title = "China and Taiwan names"
description = '''Names of China and Taiwan seems not to be matching the documentation. As I understand it, the name=* is supposed to be the default (common?) name while the official_name=* should be the fully qualified name. Here&#x27;s the difference between what I think should be mapped (according to the OSM Wiki docum...'''
date = "2016-01-10T11:46:00Z"
lastmod = "2019-04-12T22:38:00Z"
weight = 47439
keywords = [ "taiwan", "china", "name", "tagging" ]
aliases = [ "/questions/47439" ]
osqa_answers = 7
osqa_accepted = false
+++

<div class="headNormal">

# [China and Taiwan names](/questions/47439/china-and-taiwan-names)

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
<span id="post-47439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47439-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-47439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Names of China and Taiwan seems not to be matching <a href="https://wiki.openstreetmap.org/wiki/Names">the documentation</a>. As I understand it, the <code>name=*</code> is supposed to be the default (common?) name while the <code>official_name=*</code> should be the fully qualified name.</p>
<p>Here's the difference between what I think should be mapped (according to the OSM Wiki documentation and Wikipedia articles) and what is currently mapped:</p>
<table data-border="1">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th><em>China</em></th>
<th>Proposal<br />
from <a href="https://en.wikipedia.org/wiki/China">Wikipedia</a></th>
<th>Existing<br />
<a href="https://www.openstreetmap.org/relation/270056">relation object</a></th>
<th>Existing<br />
<a href="https://www.openstreetmap.org/node/424313582">node object</a></th>
</tr>
&#10;<tr>
<td><code>name=</code><br />
<code>name:en=</code></td>
<td><center>
中国<br />
China
</center></td>
<td><center>
中国<br />
China
</center></td>
<td><center>
<font>中华人民共和国<br />
People's Republic of China</font>
<center>
</center>
</center></td>
</tr>
<tr>
<td><code>official_name=</code><br />
<code>official_name:en=</code></td>
<td><center>
中华人民共和国<br />
People's Republic of China
</center></td>
<td><center>
中华人民共和国<br />
People's Republic of China
</center></td>
<td><center>
中华人民共和国<br />
People's Republic of China
</center></td>
</tr>
<tr>
<td><em>Taiwan</em></td>
<td>Proposal<br />
from <a href="https://en.wikipedia.org/wiki/Taiwan">Wikipedia</a></td>
<td>Existing<br />
<a href="https://www.openstreetmap.org/relation/449220">relation object</a></td>
<td>Existing<br />
<a href="https://www.openstreetmap.org/node/432425099">node object</a></td>
</tr>
<tr>
<td><code>name=</code><br />
<code>name:en=</code></td>
<td><center>
臺灣<br />
Taiwan
</center></td>
<td><center>
<font>中華民國<br />
Republic of China</font>
</center></td>
<td><center>
<font>中華民國<br />
Republic of China</font>
<center>
</center>
</center></td>
</tr>
<tr>
<td><code>official_name=</code><br />
<code>official_name:en=</code></td>
<td><center>
中華民國<br />
Republic of China
</center></td>
<td><center>
中華民國<br />
Republic of China
</center></td>
<td><center>
[null]
</center></td>
</tr>
</tbody>
</table>
<p><br />
</p>
<p>I'm really tempted to modify the data straight away but I thought it might be better to have an agreement with the community as it is about country names which I consider to be quite an important data.</p>
<p>Thanks to Supaplex, I am now aware of an <a href="https://www.openstreetmap.org/changeset/34099411">edit war</a> going on between using “Taiwan” or “Republic of China” in the name tag of the relation object. Here are my thoughts (in favor of “Taiwan”):</p>
<ul>
<li>The OpenStreetMap wiki clearly mention to use the common name. IMHO Taiwan is the common name used both in Taiwan and the rest of the world (except in China maybe? but then what is the common name there?). I never heard of “Republic of China” until I became more interested about the subject. A quick Google query will clearly proves it.</li>
<li>In case of disputes the OpenStreetMap wiki indicates to use ground information which I believe is very easy for identifying a city or street name but where do you look on the ground for a country name? Maybe the documentation isn’t precise enough in this case. Any advice appreciated.</li>
<li>The same dispute as been going on in the Wikipedia article where pages and pages of vigorous discussion were written. Their policy defines using <a href="https://en.wikipedia.org/wiki/Wikipedia:Article_titles#Non-neutral_but_common_names">non-neutral but common names</a>. The edit war seems to have been solved by semi-protecting the article and using Taiwan as name of the article.</li>
<li>All the other major concurrent maps I can think of are displaying Taiwan. The Natural Earth data set (<a href="http://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-0-countries/)">http://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-0-countries/)</a> also use Taiwan in its default/first name.</li>
<li>The “Republic of China (Taiwan)” and similar other combined names often used in official documentations isn’t relevant to me, <a href="https://wiki.openstreetmap.org/wiki/Disputes#Solving_Disputes">as written in the documentation</a> “<em>if there are two common versions of a place name, the "name" tag could contain them both</em>” but only one name is common here: “Taiwan”.</li>
</ul>
<p>Thanks for your feedback!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-taiwan" rel="tag" title="see questions tagged &#39;taiwan&#39;">taiwan</span> <span class="post-tag tag-link-china" rel="tag" title="see questions tagged &#39;china&#39;">china</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jan '16, 11:46</strong></p>
<img src="https://secure.gravatar.com/avatar/6b4c312d5650cdf36c9d76c184ff7d22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="freayd&#39;s gravatar image" />
<p><span>freayd</span><br />
<span class="score" title="116 reputation points">116</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="freayd has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jan '16, 10:28</strong> </span></p>
</div>
</div>
<div id="comments-container-47439" class="comments-container">
<span id="47462"></span>
<div id="comment-47462" class="comment">
<div id="post-47462-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>did you try to contact the mappers that have set the current names ?</p>
</div>
<div id="comment-47462-info" class="comment-info">
<span class="comment-age">(12 Jan '16, 06:06)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="47480"></span>
<div id="comment-47480" class="comment">
<div id="post-47480-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's actually a good idea. I haven't, it's a bit messy with lots of changesets, I'll try to get in touch with the mappers. Interestingly, the China relation have been named to what I consider correct by a Chinese mapper on <a href="https://www.openstreetmap.org/changeset/32486290">this changeset</a>.</p>
</div>
<div id="comment-47480-info" class="comment-info">
<span class="comment-age">(12 Jan '16, 13:56)</span> <span class="comment-user userinfo">freayd</span>
</div>
</div>
<span id="47537"></span>
<div id="comment-47537" class="comment">
<div id="post-47537-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you actually a local?</p>
</div>
<div id="comment-47537-info" class="comment-info">
<span class="comment-age">(16 Jan '16, 13:21)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="47544"></span>
<div id="comment-47544" class="comment">
<div id="post-47544-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No I'm not, I only traveled a few month in both countries. I guess it'll be more interesting to have other Chinese and Taiwanese joining the discussion (even thought it might imply an endless semi-political debate).</p>
</div>
<div id="comment-47544-info" class="comment-info">
<span class="comment-age">(16 Jan '16, 22:58)</span> <span class="comment-user userinfo">freayd</span>
</div>
</div>
<span id="65628"></span>
<div id="comment-65628" class="comment">
<div id="post-65628-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It looks like this has been fixed now, name=Taiwan, official_name=Republic of China.</p>
</div>
<div id="comment-65628-info" class="comment-info">
<span class="comment-age">(29 Aug '18, 12:09)</span> <span class="comment-user userinfo">aharvey</span>
</div>
</div>
</div>
<div id="comment-tools-47439" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47439-form-container" class="comment-form-container">
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

<span id="47532"></span>

<div id="answer-container-47532" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47532-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47532-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-47532-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm a Taiwanese mapper, you can see my user name of one of the history version related to Taiwan relation.</p>
<p>I commented on changeset for the one who use "中華民國" (Republic of China) as name, set "臺灣" (Taiwan) as alt_name, but he didn't response. Afraiding of editing war I didn't change back immediately, and start a discussion on <a href="https://osmtw.hackpad.com/eABxvpQKPFI">Hackpad</a> (in Chinese). Unfortunately there's few one response.</p>
<p>I think using Taiwan as common name is common sense, as a citizen we use the official national name few. Some of my mapper friends think it as well. The local mappers community in Taiwan is <a href="https://www.facebook.com/groups/OpenStreetMap.TW/permalink/975508359181300/">aware</a> of this situation, but we're mainly focus on more local stuff like drawing missing roads.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jan '16, 04:49</strong></p>
<img src="https://secure.gravatar.com/avatar/23870311518577d6069b8e79482282a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Supaplex&#39;s gravatar image" />
<p><span>Supaplex</span><br />
<span class="score" title="130 reputation points">130</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Supaplex has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jan '16, 04:49</strong> </span></p>
</div>
</div>
<div id="comments-container-47532" class="comments-container">
<span id="47535"></span>
<div id="comment-47535" class="comment">
<div id="post-47535-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks both for your feedback with local knowledge and efforts on trying to solve the issue. I agree with you and edited my question in order to reflect my arguments. I think we need to find a consensus before editing anything else. Hopefully more people will get involved into the discussion.</p>
<p>This is more on the side of the main debate but I think alt_name should contain 台灣.</p>
</div>
<div id="comment-47535-info" class="comment-info">
<span class="comment-age">(16 Jan '16, 10:41)</span> <span class="comment-user userinfo">freayd</span>
</div>
</div>
</div>
<div id="comment-tools-47532" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47532-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47452"></span>

<div id="answer-container-47452" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47452-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A collection for this point (next to the "Names" article) is created in the OSM wiki about <a href="http://wiki.openstreetmap.org/wiki/Multilingual_names">Multilingual_names</a>, and there we even have an example for China.</p>
<p>Without having dived into details myself, maybe you can find hints there:</p>
<p>Is the OSM data correct, or really needs an update?</p>
<p>Or is the documentation in the OSM wiki out-of-date, and the wiki needs a detailes update there?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jan '16, 17:24</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span> </br></br></p>
</div>
</div>
<div id="comments-container-47452" class="comments-container">
<span id="47478"></span>
<div id="comment-47478" class="comment">
<div id="post-47478-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer but I think we are misunderstanding. I know the multilingual documentation, there's no problem with it, it's up to date. The problem is really about the data which, IMHO, needs to be updated to match what the documentation says about name vs official_name. I've updated my question to include the existing values hoping it's now more obvious.</p>
</div>
<div id="comment-47478-info" class="comment-info">
<span class="comment-age">(12 Jan '16, 13:41)</span> <span class="comment-user userinfo">freayd</span>
</div>
</div>
</div>
<div id="comment-tools-47452" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47452-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47546"></span>

<div id="answer-container-47546" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47546-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47546-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47546-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm a Taiwanese mapper too. I agree with Wikipedia way to map it. We usually call ourselves as Taiwan, only in official document will name as Republic of China.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jan '16, 12:13</strong></p>
<img src="https://secure.gravatar.com/avatar/d7a057aefa836725ffe30daaa7a03ba9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vintagejhan&#39;s gravatar image" />
<p><span>Vintagejhan</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vintagejhan has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-47546" class="comments-container">
<span id="47547"></span>
<div id="comment-47547" class="comment">
<div id="post-47547-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Perfect, thank you for your help!</p>
</div>
<div id="comment-47547-info" class="comment-info">
<span class="comment-age">(17 Jan '16, 13:22)</span> <span class="comment-user userinfo">freayd</span>
</div>
</div>
</div>
<div id="comment-tools-47546" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47546-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49482"></span>

<div id="answer-container-49482" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49482-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>where do you look on the ground for a country name?</p>
</blockquote>
<p>Many ways:</p>
<ul>
<li>Go to the country, and start asking people "What country is this?".</li>
<li>What do people/companies/organisations in it, use to refer to the country? e.g. is there is a tourist information association? What do they used to refer to it? Does a newspaper claim "The best selling newspaper in ....".</li>
<li>Are there organisations/companies that include a country name, which do they use? Is there a "National Farmers Association of ..." group? Trade union groups? Business owner groups.</li>
</ul>
<p>You can use official goverment sources or documents/bodies (i.e. what does it say on the passport, what does the state owned TV stations use, etc), however that is good for getting the <code>official_name</code>, which might be different from the <code>name</code>. In the event of a naming dispute, government bodies will often doggedly stick to the official government position, so this is often not a good way to find the <code>name</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '16, 14:38</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Apr '16, 15:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></br></p>
</div>
</div>
<div id="comments-container-49482" class="comments-container">
<span id="50715"></span>
<div id="comment-50715" class="comment">
<div id="post-50715-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does changing the name to "Taiwan" confuse people looking for Kinmen and Matsu? Does anyone from Kinmen or Matsu know how you would answer "what country is this?"</p>
</div>
<div id="comment-50715-info" class="comment-info">
<span class="comment-age">(07 Jul '16, 17:25)</span> <span class="comment-user userinfo">miklcct</span>
</div>
</div>
</div>
<div id="comment-tools-49482" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49482-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50162"></span>

<div id="answer-container-50162" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50162-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I had raised the issue on <a href="https://www.facebook.com/groups/OpenStreetMap.TW/permalink/975508359181300/">Taiwan OpenStreetMap Facebook Group</a>, but few response. And the users response said they prefer using the much commonly use Taiwan in name tag.</p>
<p>It's been a long time we discuss the issue. So I change to origin name of Taiwan. I'm open-mind about other option like 臺灣(中華民國) Taiwan(Repulbic of China), or 臺灣/中華民國 Taiwan/Republic of China.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jun '16, 17:09</strong></p>
<img src="https://secure.gravatar.com/avatar/23870311518577d6069b8e79482282a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Supaplex&#39;s gravatar image" />
<p><span>Supaplex</span><br />
<span class="score" title="130 reputation points">130</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Supaplex has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jun '16, 06:30</strong> </span></p>
</div>
</div>
<div id="comments-container-50162" class="comments-container">
<span id="50164"></span>
<div id="comment-50164" class="comment">
<div id="post-50164-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>s/中華國民/中華民國/</p>
</div>
<div id="comment-50164-info" class="comment-info">
<span class="comment-age">(12 Jun '16, 18:22)</span> <span class="comment-user userinfo">kcwu</span>
</div>
</div>
</div>
<div id="comment-tools-50162" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50162-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49479"></span>

<div id="answer-container-49479" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49479-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A new Chinese Mapper (I think) change Taiwan name to their prefer name "台湾省"(Taiwan Province)</p>
<p><a href="https://www.openstreetmap.org/changeset/38946725">https://www.openstreetmap.org/changeset/38946725</a></p>
<p>The Taiwanese mapper have already change back the edit.</p>
<p>I think its time to determine if we choose the more common use common name "臺灣" for Taiwan</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '16, 14:07</strong></p>
<img src="https://secure.gravatar.com/avatar/23870311518577d6069b8e79482282a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Supaplex&#39;s gravatar image" />
<p><span>Supaplex</span><br />
<span class="score" title="130 reputation points">130</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Supaplex has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Apr '16, 05:24</strong> </span></p>
</div>
</div>
<div id="comments-container-49479" class="comments-container">
&#10;</div>
<div id="comment-tools-49479" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49479-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68777"></span>

<div id="answer-container-68777" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68777-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68777-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68777-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In support of free &amp; Open principles, it would be best to stick with Taiwan imo</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '19, 22:38</strong></p>
<img src="https://secure.gravatar.com/avatar/79fff8a35e827e376cc241510a8318bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="greyim&#39;s gravatar image" />
<p><span>greyim</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="greyim has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-68777" class="comments-container">
&#10;</div>
<div id="comment-tools-68777" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68777-form-container" class="comment-form-container">
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

