+++
type = "question"
title = "Finding Voltage information for Power Lines"
description = '''None of the electricity pylons (towers) or poles I have surveyed (in UK) have notices saying what the voltage of the line is.  Is it possible to determine the voltage being used from the shape or size of the pylons, poles or cable insulators? If so are pictures or a reference source available? How e...'''
date = "2011-09-13T13:03:00Z"
lastmod = "2011-10-19T19:00:00Z"
weight = 7831
keywords = [ "voltage", "power" ]
aliases = [ "/questions/7831" ]
osqa_answers = 7
osqa_accepted = true
+++

<div class="headNormal">

# [Finding Voltage information for Power Lines](/questions/7831/finding-voltage-information-for-power-lines)

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
<span id="post-7831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7831-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>None of the electricity pylons (towers) or poles I have surveyed (in UK) have notices saying what the voltage of the line is.<br />
</p>
<p>Is it possible to determine the voltage being used from the shape or size of the pylons, poles or cable insulators? If so are pictures or a reference source available?<br />
How else might voltage information be obtained?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-voltage" rel="tag" title="see questions tagged &#39;voltage&#39;">voltage</span> <span class="post-tag tag-link-power" rel="tag" title="see questions tagged &#39;power&#39;">power</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Sep '11, 13:03</strong></p>
<img src="https://secure.gravatar.com/avatar/6edb4957e57770118c3b8022cfce68a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srbrook&#39;s gravatar image" />
<p><span>srbrook</span><br />
<span class="score" title="993 reputation points">993</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srbrook has 3 accepted answers">13%</span> </br></br></p>
</div>
</div>
<div id="comments-container-7831" class="comments-container">
<span id="7854"></span>
<div id="comment-7854" class="comment">
<div id="post-7854-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't worry about recording what I don't know. I asked the question as I didn't know how the voltage information shown for some lines in the UK on <a href="http://www.itoworld.com/product/data/ito_map/main?view=4">http://www.itoworld.com/product/data/ito_map/main?view=4</a> was collected.</p>
</div>
<div id="comment-7854-info" class="comment-info">
<span class="comment-age">(14 Sep '11, 13:20)</span> <span class="comment-user userinfo">srbrook</span>
</div>
</div>
</div>
<div id="comment-tools-7831" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7831-form-container" class="comment-form-container">
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

<span id="8513"></span>

<div id="answer-container-8513" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8513-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="srbrook has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Did you see the recommendations on <a href="http://wiki.openstreetmap.org/wiki/Key:power">Key:power</a>?</p>
<blockquote>
<p>National Grid call the things "towers" as they're free-standing, but common usage seems to be "pylon"</p>
<p>In the UK, each power line appears to have a two character identifier and each tower along that line appears to be numbered. For example ZM is the West Weybridge to Chessington line, and each tower is numbered ZM 1, ZM 2, etc. I propose that these be recorded, if known, for each tower with the ref tag. For example: power=tower, ref=ZM 35.</p>
<p>In the UK there is a hierarchy of power lines that is easy to identify. Most are identifiable over long distances which makes them useful for navigation. Other countries follow very similar schemes (not surprising as the design is constrained by the same physics and economics). Starting at the low-voltage end, we have:</p>
<ul>
<li>Wooden poles carrying four wires on small ceramic insulators, or bundles of insulated cables twisted together. These lines are usually 400 V between phases, which directly provide the domestic 230 V supply. Most of these follow roads and paths.</li>
<li>Wooden poles with two or three widely-spaced bare wires on large insulators having one or two plates. These lines are 11,000 volts - often used for distribution in rural areas.</li>
<li>Wooden poles with three bare wires on multi-plate insulators are 45,000 V between phases - usually on higher and more substantial poles, sometimes poles are used in pairs.</li>
<li>Metal towers carrying a set of single wires (usually three plus an earth wire on top) are 132,000 V. These are gradually disappearing.</li>
<li>Towers with three or six double wires are 275,000 V</li>
<li>Towers with three or six quadruple wires are 400,000 V</li>
</ul>
</blockquote>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '11, 19:00</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-8513" class="comments-container">
&#10;</div>
<div id="comment-tools-8513" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8513-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7832"></span>

<div id="answer-container-7832" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7832-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7832-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-7832-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I recommend not worrying about it - there are plenty of more useful things to map than what voltage a power cable is.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Sep '11, 13:19</strong></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomH has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-7832" class="comments-container">
<span id="7973"></span>
<div id="comment-7973" class="comment">
<div id="post-7973-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is it really necessary to record the voltages? The result of doing so is to have "CAVIDOTTO (400000 VOLT)" written large across the complete width of the screen of my Garmin GPS60 as I approach powerlines. A bit offputting when trying to navigate.</p>
</div>
<div id="comment-7973-info" class="comment-info">
<span class="comment-age">(18 Sep '11, 15:31)</span> <span class="comment-user userinfo">chrisboucher</span>
</div>
</div>
<span id="7974"></span>
<div id="comment-7974" class="comment">
<div id="post-7974-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I would only expect it to do that if somebody has put the voltage in the name, and even then you would have to chosen to include the names of power lines (an odd thing to do) when the Garmin map was generated.</p>
<p>I suspect that your problem is really with the author the style sheet used to render your Garmin maps.</p>
</div>
<div id="comment-7974-info" class="comment-info">
<span class="comment-age">(18 Sep '11, 15:34)</span> <span class="comment-user userinfo">TomH ♦♦</span>
</div>
</div>
</div>
<div id="comment-tools-7832" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7832-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7834"></span>

<div id="answer-container-7834" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7834-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7834-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-7834-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First, remember that you don't have to record the voltage for power lines. You can omit any information from OpenStreetMap that is too difficult/dangerous to collect.</p>
<p>However, if you do want to record the information, you can tell the voltage by the type of pole/pylon used. Search engines is your friend in identifying which is which.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Sep '11, 13:56</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Sep '11, 15:08</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span></p>
</div>
</div>
<div id="comments-container-7834" class="comments-container">
&#10;</div>
<div id="comment-tools-7834" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7834-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7835"></span>

<div id="answer-container-7835" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7835-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7835-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-7835-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Usually it is true that higher voltages have bigger/higher towers, but concrete sizes and shapes are very country specific and even within one country various types are used for the same voltage (eg. straight, direction change...). I have no idea how they look in UK.<br />
Commonly there are only a few voltages used - this makes it easier to guess in the Czech Republic it is 400V, 22kV, 110kV, 200kV and 400kV. You can look <a href="http://www.tzb-info.cz/4183-stozary-vvn-ii">here</a> for some pictures (in czech).<br />
Each power line will have start and end: a power plant, some power station or a transformer. On transformers it is usually written what voltages they transform.<br />
Unfortunately there is no easy universal solution to get the voltage by looking at the poles/wires.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Sep '11, 14:13</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span> </br></br></p>
</div>
</div>
<div id="comments-container-7835" class="comments-container">
&#10;</div>
<div id="comment-tools-7835" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7835-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7875"></span>

<div id="answer-container-7875" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7875-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I wouldn't rely absolutely on the following as it is recalled from college a fair while ago!</p>
<p>In the UK the National Grid operates at three voltages: 132Kv, 275Kv and 400Kv. Distribution at higher voltages is more prone to losses and problems caused by corona discharge. To reduce this, the <em>effective</em> diameter of the individual transmission cable is increased. This is achieved by adding more 'wires' to create a bundle conductor. 132Kv is usually distributed using single strand cables. 220Kv use pairs and 400Kv uses quads. This is only relevant on the National Grid using pylon towers and is a guide rather than an absolute truth! (And, yes, I'm aware of some transmission lines using triples - I've no idea when these are used!)</p>
<p>I wouldn't tag using the above info.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Sep '11, 19:46</strong></p>
<img src="https://secure.gravatar.com/avatar/ec180fe051c382b214977ae4a8bf85e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="G3YAC&#39;s gravatar image" />
<p><span>G3YAC</span><br />
<span class="score" title="516 reputation points">516</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="G3YAC has 2 accepted answers">20%</span> </br></p>
</div>
</div>
<div id="comments-container-7875" class="comments-container">
&#10;</div>
<div id="comment-tools-7875" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7875-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8491"></span>

<div id="answer-container-8491" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8491-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>try looking at the insulators, the higher the voltage the larger the number of insulators between the tower and the conductor. The insulators are the glass dishes hanging from the tower crossarm points and connecting to the conductor</p>
<p>robin</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Oct '11, 21:53</strong></p>
<img src="https://secure.gravatar.com/avatar/82635bdcc33185db4f3f2f8b9310bccd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robin2369&#39;s gravatar image" />
<p><span>robin2369</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robin2369 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8491" class="comments-container">
&#10;</div>
<div id="comment-tools-8491" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8491-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8504"></span>

<div id="answer-container-8504" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8504-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, roughly estimating you can count 100kV for every meter of insulator. But dont try to climb up and measure it ;-)</p>
<p>But many power lines may hang on older insulators with the ability for more voltage (not the other way round).</p>
<p>To be sure, you should have a deeper look at the lines just outside a sub station. Lines of the same voltage come together at the same part of the sub station, connected by busbars. If a sub station is fed by several voltages, you find a transformer between the parts of that sub station. A 110kV-to-medium-voltage transformer has the size of a garage, while 220/110kV and 380/110kV are quiet larger.</p>
<p>ajoessen</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '11, 12:48</strong></p>
<img src="https://secure.gravatar.com/avatar/baddeab22266e1533be4ba4c9f3deb49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajoessen&#39;s gravatar image" />
<p><span>ajoessen</span><br />
<span class="score" title="168 reputation points">168</span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajoessen has one accepted answer">9%</span></p>
</div>
</div>
<div id="comments-container-8504" class="comments-container">
&#10;</div>
<div id="comment-tools-8504" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8504-form-container" class="comment-form-container">
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

