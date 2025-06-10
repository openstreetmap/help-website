+++
type = "question"
title = "How do I denote a business is not yet open or has shut down?"
description = '''One way to do it is probably to mark it as an address with no business information. Or I can name it, but put in parentheses the status (not open yet or closed down). I could also leave a note for someone to update this information later. Another route for if it&#x27;s not yet open would be to just leave...'''
date = "2019-01-25T01:25:00Z"
lastmod = "2019-01-25T20:15:00Z"
weight = 67728
keywords = [ "construction", "unavailable", "tagging" ]
aliases = [ "/questions/67728" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How do I denote a business is not yet open or has shut down?](/questions/67728/how-do-i-denote-a-business-is-not-yet-open-or-has-shut-down)

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
<span id="post-67728-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67728-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67728-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>One way to do it is probably to mark it as an address with no business information. Or I can name it, but put in parentheses the status (not open yet or closed down). I could also leave a note for someone to update this information later.</p>
<p>Another route for if it's not yet open would be to just leave this data out and I (or someone else) will need to add it later when it's open. What I'd like to do is use construction=yes, but I assume it'll still show up on the map and be confusing to people who don't know it's not open.</p>
<p>Please advise on the best path to take. If it's shut down but all the business markings are still there, I assume we just leave out/remove this data right?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-construction" rel="tag" title="see questions tagged &#39;construction&#39;">construction</span> <span class="post-tag tag-link-unavailable" rel="tag" title="see questions tagged &#39;unavailable&#39;">unavailable</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jan '19, 01:25</strong></p>
<img src="https://secure.gravatar.com/avatar/12066cbfd8fce49065b384d49de5e707?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pluto%20is%20a%20Planet&#39;s gravatar image" />
<p><span>Pluto is a P...</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pluto is a Planet has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67728" class="comments-container">
<span id="67741"></span>
<div id="comment-67741" class="comment">
<div id="post-67741-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>The given answers give excellent advice about how to handle these cases. I'd just like to add that putting a status into the name would be considered very wrong.</p>
</div>
<div id="comment-67741-info" class="comment-info">
<span class="comment-age">(25 Jan '19, 16:41)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-67728" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67728-form-container" class="comment-form-container">
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

<span id="67732"></span>

<div id="answer-container-67732" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67732-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67732-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-67732-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Pluto is a Planet has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>For a POI that is not yet to be constructed, <strong>do not add it on OSM</strong>.</li>
<li><p>For a POI that its construction is in progress, <strong>add your data, but prefix the POI type key with <a href="https://wiki.openstreetmap.org/wiki/Key:construction"><code>construction:</code></a> <a href="https://wiki.openstreetmap.org/wiki/Lifecycle_prefix">lifecycle prefix</a></strong>. This prefix will prevent your not-yet-open POI from displaying on the maps/applications in an inappropriate way.</p>
<p>For example (node-type POI):</p>
<pre><code>construction:shop=convenience
name=7-Eleven</code></pre>
<p>Which, once open for business, you can remove the prefix; turning it into:</p>
<pre><code>shop=convenience
name=7-Eleven</code></pre>
<p>In case you have other information (like <a href="https://wiki.openstreetmap.org/wiki/Key:phone"><code>phone=*</code></a>, <a href="https://wiki.openstreetmap.org/wiki/Key:opening_hours"><code>opening_hours=*</code></a>), you may add them if you wish. (<a href="https://wiki.openstreetmap.org/wiki/Verifiability">May the verifiability be with you</a>) Applications, as far as I figured, would not take them seriously if the POI is in construction or closed down.</p>
<p>If said POI is also building-in-construction (way-type POI), <strong>consider adding <a href="https://wiki.openstreetmap.org/wiki/Tag:building%3Dconstruction">building-specific <code>building=construction</code>, <code>construction=*</code> combo</a> too</strong>; for example:</p>
<pre><code>building=construction
construction=retail
construction:shop=mall
name=Zen</code></pre>
<p>Which, once open for business, you can turn it into:</p>
<pre><code>building=retail
shop=mall
name=Zen</code></pre></li>
<li><p>For a POI that recently went out of business, <strong>prefix the POI type key with <a href="https://wiki.openstreetmap.org/wiki/Key:disused:"><code>disused:</code></a></strong> . This will remove it from most maps/applications display.</p>
<ul>
<li>If the sign is still there, you can leave other data intact.</li>
<li>If the sign is removed, then you can remove other information that is specific to the closed business. Leave other standing information, like address, and disuse-prefixed shop type, intact.
<ul>
<li>Note: If locals still know or call it by the old name, you might consider changing <a href="https://wiki.openstreetmap.org/wiki/Key:name"><code>name=*</code></a> key into <a href="https://wiki.openstreetmap.org/wiki/Key:old_name"><code>old_name=*</code></a> instead of removing it outright.</li>
</ul></li>
<li>If the POI is also a building, keep those building-related tags intact.</li>
</ul>
<p>For example, a <a href="https://wiki.openstreetmap.org/wiki/Tag:shop%3Dgas">bottled gas shop</a>, that is also a building:</p>
<pre><code>building=retail
shop=gas
name=Wang Gas
opening_hours=08:00-16:00;PH closed
addr:housenumber=123
addr:street=Merry Street</code></pre>
<p>When it's out of business:</p>
<pre><code>building=retail
disused:shop=gas
name=Wang Gas
opening_hours=08:00-16:00;PH closed
addr:housenumber=123
addr:street=Merry Street</code></pre>
<p>When its sign is taken down:</p>
<pre><code>building=retail
disused:shop=gas
addr:housenumber=123
addr:street=Merry Street</code></pre></li>
</ol>
<p>P.S. If the POI is not just closed down, but also in a very bad shape (e.g. windows/walls falling down), consider using <a href="https://wiki.openstreetmap.org/wiki/Key:abandoned"><code>abandoned:</code></a> prefix in place of <code>disused:</code>.</p>
<p>P.P.S. If the entire block or building got torn down, then you can just remove all information/sub-POIs inside it. (Also consider marking the area with <a href="https://wiki.openstreetmap.org/wiki/Tag:landuse%3Dbrownfield"><code>landuse=brownfield</code></a> if you see fit) Don't forget to note the fact on <a href="https://wiki.openstreetmap.org/wiki/Good_changeset_comments">edit summary</a> when saving your edit too, or otherwise people would think you were vandalizing the map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '19, 04:18</strong></p>
<img src="https://secure.gravatar.com/avatar/d0bf78fa6f7ca788533635c1bb605e12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nutchanon%20Wetchasit&#39;s gravatar image" />
<p><span>Nutchanon We...</span><br />
<span class="score" title="290 reputation points">290</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nutchanon Wetchasit has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jan '19, 12:09</strong> </span></p>
</div>
</div>
<div id="comments-container-67732" class="comments-container">
&#10;</div>
<div id="comment-tools-67732" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67732-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67729"></span>

<div id="answer-container-67729" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67729-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67729-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-67729-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In practice people do all those things.</p>
<p>For new stuff I would say mapping the address is a good way to handle it, and then maybe add a note stating when the business is opening (a note on the osm website preferably vs a <code>note=</code> tag). People use the notes as todo items, so it should eventually get fixed up.</p>
<p>For a closed business that still has signs and such, I think removing the key tag (probably <code>shop=</code> or <code>amenity=</code>) is a good way to do it. It's still identifiable by the name, it just doesn't offer services. If the signs are gone, the name can come off.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '19, 03:12</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-67729" class="comments-container">
&#10;</div>
<div id="comment-tools-67729" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67729-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67730"></span>

<div id="answer-container-67730" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67730-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67730-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67730-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know if there is a standard way to tag future things but this is what I do:</p>
<ul>
<li>Use the construction: prefix for the future tags. For example construction:name=futurename, construction:amenity=restaurant, construction:website=<a href="http://website.for.new.business">http://website.for.new.business</a></li>
<li>I add a fixme tag with a description of the situation. For example fixme="Was the xyz restaurant, is currently being remodeled to become the abc restaurant, expected opening spring 2019". The use of the fixme tag helps me remember to check back from time to time to see if they are now open. And if I don't do it, then some other mapper may see the fixme tag and do the check.</li>
</ul>
<p>For businesses that have gone away, I change the place to shop=vacant and add a description="Used to be the xyz store, now empty." If/when another business opens in that location then I update everything to the new business and drop anything that refers to the old business (OSM is supposed to be for current data).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '19, 03:20</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-67730" class="comments-container">
<span id="67733"></span>
<div id="comment-67733" class="comment">
<div id="post-67733-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>shop=vacant sells ... vacants? ;-) Not a good tag for a renderer which just renders all shops - but does not know this exception.</p>
</div>
<div id="comment-67733-info" class="comment-info">
<span class="comment-age">(25 Jan '19, 06:35)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="67735"></span>
<div id="comment-67735" class="comment">
<div id="post-67735-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Got a point, but I found it in the wiki <a href="https://wiki.openstreetmap.org/wiki/Tag:shop%3Dvacant">https://wiki.openstreetmap.org/wiki/Tag:shop%3Dvacant</a> as well as near the bottom of <a href="https://wiki.openstreetmap.org/wiki/Key:shop">https://wiki.openstreetmap.org/wiki/Key:shop</a></p>
</div>
<div id="comment-67735-info" class="comment-info">
<span class="comment-age">(25 Jan '19, 08:40)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="67742"></span>
<div id="comment-67742" class="comment">
<div id="post-67742-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>shop=malls don't sell shopping centres either. the disused prefix covers too many eventualities to identify shops which don't CURRENTLY have a tenant. It has the merit of being duck tagging: people actually talk about empty or vacant shops (which is more than I can say for malls). It also assumes the only use case for shop is to find things to buy, which is not the case.</p>
</div>
<div id="comment-67742-info" class="comment-info">
<span class="comment-age">(25 Jan '19, 16:48)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="67743"></span>
<div id="comment-67743" class="comment">
<div id="post-67743-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5918/stf"></a><a href="https://help.openstreetmap.org/users/5918/stf">@stf</a>: Both of those places in the wiki also add some words of caution, though, which I agree with. Given how many shop values there are, and how many keep being added, it makes data consumers' work easier if they can just treat all <code>shop=*</code> tags as shops. After all, <code>shop=*</code> is defined as "a place selling retail products or services".</p>
</div>
<div id="comment-67743-info" class="comment-info">
<span class="comment-age">(25 Jan '19, 17:42)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="67745"></span>
<div id="comment-67745" class="comment">
<div id="post-67745-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/647/sk53"></a><a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a>: at least a shop=mall IS a kind of collection of shops. A shop=vacant is not a shop (it is just a place suitable for a shop and looking like a shop) - but would still show up in a simple rendering which just displays all shop=* (see Tordanik). Even the featured <a href="https://www.openstreetmap.org/way/164701361#map=20/49.83475/8.90188&amp;layers=H">humanitarian layer displays</a> a shop=vacant with a shop icon. And iD, too.</p>
<p>Duck tagging? It may look like a (closed) shop, but it does not sell like a shop. So, imho it fails the test for a shop. Ducks quack and shops sell. ;-)</p>
</div>
<div id="comment-67745-info" class="comment-info">
<span class="comment-age">(25 Jan '19, 20:15)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67730" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67730-form-container" class="comment-form-container">
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

