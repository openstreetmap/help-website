+++
type = "question"
title = "Address: Street name differs from Building Row name"
description = '''Hi My city has many terraced rows of buildings which have a separate name to the actual road they are adjacent to. https://wiki.openstreetmap.org/wiki/Key:addr There does appears to be a specific tag for this. &#x27;block&#x27; doesn&#x27;t quite seem appropriate &amp;amp; I&#x27;ve seen the house number &amp;amp; building row...'''
date = "2017-11-16T18:40:00Z"
lastmod = "2017-11-19T22:18:00Z"
weight = 60655
keywords = [ "tagging", "address" ]
aliases = [ "/questions/60655" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [Address: Street name differs from Building Row name](/questions/60655/address-street-name-differs-from-building-row-name)

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
<span id="post-60655-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60655-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-60655-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>My city has many terraced rows of buildings which have a separate name to the actual road they are adjacent to. <a href="https://wiki.openstreetmap.org/wiki/Key:addr">https://wiki.openstreetmap.org/wiki/Key:addr</a></p>
<p>There does appears to be a specific tag for this. 'block' doesn't quite seem appropriate &amp; I've seen the house number &amp; building row name combined to be tag with addr:housenumber. Is this acceptable or is there a better way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Nov '17, 18:40</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Nov '17, 19:00</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-60655" class="comments-container">
&#10;</div>
<div id="comment-tools-60655" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60655-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="60661"></span>

<div id="answer-container-60661" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60661-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60661-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-60661-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>SK53 missed out one option (the one that really works :-))</p>
<p>Add a place node (typically place=neighbourhood) to the area, and reference that in the addresses with addr:place instead of addr:street</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Nov '17, 09:12</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-60661" class="comments-container">
<span id="60675"></span>
<div id="comment-60675" class="comment">
<div id="post-60675-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But that is actually inaccurate tagging for these situations. These are really streetnames not small local areas. Before addresses were shoehorned into a Procrustean data model they would have been something like 10, Harlech Terrace, Holyhead Road, Bethesda. As place=neighbourhood also gets rendered there are likely other unwanted side effects.</p>
</div>
<div id="comment-60675-info" class="comment-info">
<span class="comment-age">(18 Nov '17, 15:05)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="60677"></span>
<div id="comment-60677" class="comment">
<div id="post-60677-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Neighbourhood doesn't seem appropriate. They're mostly just a row of a few houses. Not really large enough.</p>
</div>
<div id="comment-60677-info" class="comment-info">
<span class="comment-age">(18 Nov '17, 17:41)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-60661" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60661-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60657"></span>

<div id="answer-container-60657" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60657-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The following approaches are possible when the logical street name is not that of the roads. This applies to either named terraces or streets where the sides of the street are named:</p>
<ul>
<li>Put the complete address in addr:full: 8, Row, Main Street</li>
<li>Put the housenumber in addr:housenumber and the name of the terrace or row in addr:housename. (This seems to be roughly what Royal Mail do with PAF).</li>
<li>Add a footway in front the the terrace/row with the same name.</li>
<li>Use an associatedStreet relation to bind addresses to the main road, but with addr:street being the name of the row.</li>
<li>Just put the row/terrace name in addr:street and be done with it.</li>
<li>The method you mention</li>
</ul>
<p>None are wholly satisfactory, the first 3 are obvious fudges but may be legitimate in some, but not all, circumstances. The second approach makes properties in a terrace indistinguishable from houses with both a number and name. 4 &amp; 5 are accurate but are either non-obvious for data consumers or will generate false positives for QA tools. 6 I would avoid.</p>
<p>In the UK, if the row/terrace has it's own postcode you will want the addr:housenumber to be clearly searchable as this in conjunction with the postcode should uniquely identify the address.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '17, 19:14</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-60657" class="comments-container">
<span id="60678"></span>
<div id="comment-60678" class="comment">
<div id="post-60678-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As you mentions none work fully. It's a bit 'square peg, round hole'. They're either unclear or fudging it with extra data. I'll probably go with 'full' &amp; then split it if a better way appears</p>
</div>
<div id="comment-60678-info" class="comment-info">
<span class="comment-age">(18 Nov '17, 18:00)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-60657" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60657-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60658"></span>

<div id="answer-container-60658" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60658-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Addr should be the street address, street should have it's own name. Weird, but comes up a bit in Oklahoma.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '17, 22:58</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-60658" class="comments-container">
<span id="60679"></span>
<div id="comment-60679" class="comment">
<div id="post-60679-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unsure what you mean.</p>
</div>
<div id="comment-60679-info" class="comment-info">
<span class="comment-age">(18 Nov '17, 18:01)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-60658" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60658-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60672"></span>

<div id="answer-container-60672" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60672-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I mapped these new named terraces a few years ago, they render ok but searching only partly works. EDIT 'I didn't use the same method on each block as i was hoping that i would find out which got the result, for example 12 churchill terrace buttsgrove way, i then had to wait for the search engines absorb the data. From memory i checked back a few times but didn't find what i was looking for'. Comments from addressing and searching experts welcome. <a href="https://www.openstreetmap.org/#map=19/52.33992/-0.16875">https://www.openstreetmap.org/#map=19/52.33992/-0.16875</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Nov '17, 07:49</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Nov '17, 20:02</strong> </span></p>
</div>
</div>
<div id="comments-container-60672" class="comments-container">
<span id="60680"></span>
<div id="comment-60680" class="comment">
<div id="post-60680-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How would you amalgamate them so they're all addr:* tags</p>
</div>
<div id="comment-60680-info" class="comment-info">
<span class="comment-age">(18 Nov '17, 18:03)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-60672" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60672-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60699"></span>

<div id="answer-container-60699" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60699-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60699-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60699-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've seen <code>name:left=*</code> / <code>name:right=*</code> used in some places on streets where there is a terrace with a different name to that of the street.</p>
<p><code>highway=footway</code> + <code>footway=sidewalk</code> + <code>name=*</code> in front of the terrace could be another option.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '17, 14:15</strong></p>
<img src="https://secure.gravatar.com/avatar/9f18ba3d13472af00b3b6e2befad85e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lakedistrict&#39;s gravatar image" />
<p><span>lakedistrict</span><br />
<span class="score" title="221 reputation points">221</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lakedistrict has one accepted answer">25%</span></p>
</div>
</div>
<div id="comments-container-60699" class="comments-container">
<span id="60706"></span>
<div id="comment-60706" class="comment">
<div id="post-60706-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm adding addr:* to specific houses</p>
</div>
<div id="comment-60706-info" class="comment-info">
<span class="comment-age">(19 Nov '17, 22:18)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-60699" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60699-form-container" class="comment-form-container">
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

