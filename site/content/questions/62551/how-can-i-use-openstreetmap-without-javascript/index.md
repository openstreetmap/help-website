+++
type = "question"
title = "How can I use OpenStreetMap without JavaScript?"
description = '''Hello, I am concerned about the Spectre and Meltdown vulnerabilities and the possibility for mischief they create for JavaScript coming from websites. So I am browsing the web with JS completely disabled. Still I have been looking for a way to use maps without JS. My question is: How can I use OpenS...'''
date = "2018-03-07T16:57:00Z"
lastmod = "2021-11-10T14:38:00Z"
weight = 62551
keywords = [ "usage", "security", "javascript" ]
aliases = [ "/questions/62551" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How can I use OpenStreetMap without JavaScript?](/questions/62551/how-can-i-use-openstreetmap-without-javascript)

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
<span id="post-62551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62551-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am concerned about the Spectre and Meltdown vulnerabilities and the possibility for mischief they create for JavaScript coming from websites. So I am browsing the web with JS completely disabled. Still I have been looking for a way to use maps without JS.</p>
<p>My question is:</p>
<p>How can I use OpenStreetMap without having to download and execute any JavaScript from external hosts? (I use a Linux system) Maybe there is some FOSS application which uses an HTTP API to OpenStreetMap (or anything along these lines)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span> <span class="post-tag tag-link-security" rel="tag" title="see questions tagged &#39;security&#39;">security</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Mar '18, 16:57</strong></p>
<img src="https://secure.gravatar.com/avatar/baae4f852ab3bf8276b1e5078f8ae428?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="t33rex&#39;s gravatar image" />
<p><span>t33rex</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="t33rex has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Mar '18, 06:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-62551" class="comments-container">
<span id="62558"></span>
<div id="comment-62558" class="comment">
<div id="post-62558-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Did you think of selectively allowing JavaScript just for specific sites? E.g. <a href="https://github.com/gorhill/uMatrix">uMatrix</a> gives you very granular control.</p>
</div>
<div id="comment-62558-info" class="comment-info">
<span class="comment-age">(07 Mar '18, 21:43)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="62600"></span>
<div id="comment-62600" class="comment">
<div id="post-62600-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note that you can reduce the risk of Spectre by viewing each website in a separate browser process.</p>
</div>
<div id="comment-62600-info" class="comment-info">
<span class="comment-age">(09 Mar '18, 09:30)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="62604"></span>
<div id="comment-62604" class="comment">
<div id="post-62604-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In the rare cases in which I enable JS for sites which don't work without it, I do it in an incognito window with all other programs stopped and clipboard contents cleared. In Chromium I also have enabled: <span>chrome://flags/#enable-site-per-process</span></p>
<p>But even this simulation of "single tasking" is not enough because shutting down a program doesn't clear the RAM contents which it used. Unfortunately this very site is forcing me to enable JS (from google.com and googleapis.com) and I cannot add comments without unblocking those in uMatrics. This is quite unfortunate and I don't see why this was chosen for a message board for a program supposedly respecting user freedom.</p>
</div>
<div id="comment-62604-info" class="comment-info">
<span class="comment-age">(09 Mar '18, 11:43)</span> <span class="comment-user userinfo">t33rex</span>
</div>
</div>
<span id="62608"></span>
<div id="comment-62608" class="comment">
<div id="post-62608-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14843/t33rex"></a><a href="https://help.openstreetmap.org/users/14843/t33rex">@t33rex</a>: regarding this site: yes, we (all, more or maybe less) know that issues, but we are (nearly - one employee) a volunteer-only project... I dislike that external google library, too. If you can, you are very welcome to help, see <a href="https://wiki.openstreetmap.org/wiki/Help.openstreetmap.org">over there "technical details"</a>. Note that there are other <a href="https://wiki.openstreetmap.org/wiki/Contact_channels">contact channels</a> which may suit you more..</p>
</div>
<div id="comment-62608-info" class="comment-info">
<span class="comment-age">(09 Mar '18, 21:36)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="82540"></span>
<div id="comment-82540" class="comment">
<div id="post-82540-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Have you see my implementation of a php mapping solution at: <a href="http://map.netzgesta.de">http://map.netzgesta.de</a> It works without any Javascript. Contact me if you want to know more.</p>
</div>
<div id="comment-82540-info" class="comment-info">
<span class="comment-age">(10 Nov '21, 14:38)</span> <span class="comment-user userinfo">manualis</span>
</div>
</div>
</div>
<div id="comment-tools-62551" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62551-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="62555"></span>

<div id="answer-container-62555" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62555-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-62555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Can you use the OpenStreetMap-provided web site without Javascript? No, not really. Can you make your own web site that displays an OSM map without Javascript? Absolutely! Since the map tiles are just PNG images, it is easy enough to write, say, a PHP application that generates a map view consisting of a series of "IMG" tags arranged in a table or properly CSS styled. You would not be able to grab the map with the mouse and move it - you'd have to click little left/right/up/down buttons on the margins of the map etc. - but it is definitely possible.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Mar '18, 18:21</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-62555" class="comments-container">
&#10;</div>
<div id="comment-tools-62555" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62555-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="62559"></span>

<div id="answer-container-62559" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62559-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-62559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As you already noticed nearly everything is possible with OSM - because our raw data is <em>free</em>.</p>
<p>If you like to just view the standard OSM map you could use a local application which shows the tiles. If you use a Linux PC: You can misuse our top editor <a href="https://wiki.openstreetmap.org/wiki/JOSM">https://wiki.openstreetmap.org/wiki/JOSM</a> for that (just do two clicks and display the OSM Carto map as background layer; hey, and maybe you even like to contribute to OSM ...). JOSM is FOSS and written in Java. However, if you would like to inspect the code there are surely muuuuch more lightweight software which just displays a pre-made map. See <a href="https://wiki.openstreetmap.org/wiki/Software/Desktop">https://wiki.openstreetmap.org/wiki/Software/Desktop</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Mar '18, 21:51</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Mar '18, 23:02</strong> </span></p>
</div>
</div>
<div id="comments-container-62559" class="comments-container">
<span id="62561"></span>
<div id="comment-62561" class="comment">
<div id="post-62561-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the links. The last one is particularly interesting. I actually have KDE Marble installed and I gave it a try. However nothing makes it obvious whether it or any of the other programs in the desktop software list downloads and executes any external JS. For marble in particular I asked in the KDE forums but still no clear reply. Do you have any idea about all that?</p>
</div>
<div id="comment-62561-info" class="comment-info">
<span class="comment-age">(07 Mar '18, 22:36)</span> <span class="comment-user userinfo">t33rex</span>
</div>
</div>
<span id="62592"></span>
<div id="comment-62592" class="comment">
<div id="post-62592-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14843/t33rex">@t33rex</a>: no, sorry, I do not know about that marble fact. I would have guessed that it is abandoned (because I used it years ago) but <a href="https://cgit.kde.org/marble.git/log/">development seems</a> to be living. :-)</p>
</div>
<div id="comment-62592-info" class="comment-info">
<span class="comment-age">(08 Mar '18, 19:29)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="62593"></span>
<div id="comment-62593" class="comment">
<div id="post-62593-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14843/t33rex">@t33rex</a> (at the risk of wandering off topic) why the concern about particular JavaScript executed by Marble and not any other of the rest of the code?</p>
</div>
<div id="comment-62593-info" class="comment-info">
<span class="comment-age">(08 Mar '18, 19:58)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="62596"></span>
<div id="comment-62596" class="comment">
<div id="post-62596-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Because 1) I have Marble installed and 2) executing JS downloaded from external hosts is in no way different from downloading and executing any other random program. It is a very easy way to sneak in some malware through that which would not be a big problem if side channel CPU bugs didn't exist. But they do exist and now everyone knows about them and more people will start exploiting them.</p>
<p>Of course it is possible malicious code to be inserted in the local program (e.g. Marble) itself but the probability for that is much lower. It needs to be a specially designed spyware which will surely get the eyes of the community watching the program code. So although it is never an absolute trust, still the probability is much lower. Just like it is more unlikely to see malware in FOSS than in proprietary software.</p>
</div>
<div id="comment-62596-info" class="comment-info">
<span class="comment-age">(08 Mar '18, 22:36)</span> <span class="comment-user userinfo">t33rex</span>
</div>
</div>
</div>
<div id="comment-tools-62559" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62559-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="62557"></span>

<div id="answer-container-62557" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62557-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62557-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-62557-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can try <a href="https://wiki.openstreetmap.org/wiki/Mapscii">Mapscii</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Mar '18, 20:33</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-62557" class="comments-container">
<span id="62560"></span>
<div id="comment-62560" class="comment">
<div id="post-62560-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That is amazing! Thanks for sharing.</p>
</div>
<div id="comment-62560-info" class="comment-info">
<span class="comment-age">(07 Mar '18, 22:34)</span> <span class="comment-user userinfo">t33rex</span>
</div>
</div>
</div>
<div id="comment-tools-62557" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62557-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="62553"></span>

<div id="answer-container-62553" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62553-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One option is not to browse the web. Have your own <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">map server</a> local to you, serving map tiles via a website that you have complete control over, using JavaScript that you have inspected every line of.</p>
<p>Well, or only fetching the tiles (png images) from online, but hosting the HTML and JavaScript (e.g. <a href="https://wiki.openstreetmap.org/wiki/Slippy_Map">Leaflet or openlayers</a>) bits locally. No need for a map server.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Mar '18, 17:02</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Mar '18, 22:24</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-62553" class="comments-container">
<span id="62562"></span>
<div id="comment-62562" class="comment">
<div id="post-62562-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... in fact <a href="https://github.com/SomeoneElseOSM/SomeoneElse-map/blob/master/map/map.html">here's one I made earlier</a> that does exactly that. Just have "leaflet_dist" locally adjacent to the rest of the website.</p>
</div>
<div id="comment-62562-info" class="comment-info">
<span class="comment-age">(07 Mar '18, 22:50)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="62563"></span>
<div id="comment-62563" class="comment">
<div id="post-62563-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... simply locally saving the <a href="http://leafletjs.com/examples/quick-start/">http://leafletjs.com/examples/quick-start/</a> example is also an easy start.</p>
</div>
<div id="comment-62563-info" class="comment-info">
<span class="comment-age">(07 Mar '18, 23:04)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62553" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62553-form-container" class="comment-form-container">
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

