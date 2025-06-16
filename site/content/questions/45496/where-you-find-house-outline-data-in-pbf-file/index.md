+++
type = "question"
title = "Where you find house outline data in PBF file?"
description = '''Using Osmosis I&#x27;ve read the entire world PBF file. However, so far I&#x27;ve been unable to find house outline data. For example, my neighborhood in Forest Knolls, San Francisco has house outlines when viewed on the OSM website, but when I filter all the ways/nodes in the world PBF file to a bounding box...'''
date = "2015-09-22T00:25:00Z"
lastmod = "2015-09-23T03:59:00Z"
weight = 45496
keywords = [ "building", "pbf", "outlines" ]
aliases = [ "/questions/45496" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Where you find house outline data in PBF file?](/questions/45496/where-you-find-house-outline-data-in-pbf-file)

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
<span id="post-45496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45496-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Using Osmosis I've read the entire world PBF file. However, so far I've been unable to find house outline data. For example, my neighborhood in Forest Knolls, San Francisco has house outlines when viewed on the OSM website, but when I filter all the ways/nodes in the world PBF file to a bounding box of my neighborhood, I don't see house outlines. So, the question is, where can the house outline data be found in the PBF file?</p>
<p>In response to the comment requesting further information...</p>
<p>I downloaded the current "planet-latest.osm.pbf" as of about six weeks ago (the date on my copy of the file shows Aug 3, 2015). This file is about 30 GB and and contains something close to 3.5 billion records (about 3 billion nodes and about 500 million ways). When filtered to US only records it has about 560 million nodes and I forget, maybe 30 million ways.</p>
<p>Describing the full filtering process is fairly complex, since the amount of data is quite large and various algorithms I attempted exceeded my 32GB of RAM (partially because Java built-in data structures have huge amounts of overhead). So I created a fairly elaborate multipass algorithm that first filtered to find all ways and nodes in the US and wrote the data out to intermediate files and then repeated this process starting with the intermediate files to create state level files (one of course being California). Then finally filtered to a particular test neighborhood (my neighborhood in SF). So there's a lot of things that <em>could</em> have gone wrong, but if I knew where to start looking (where the house outline data is) then it would be easier for me to track what might have gone wrong.</p>
<p>So basically I'm wondering if house outlines are stored as ways, or as nodes, or what? I thought they would be stored as ways that then referred to a list of node Ids that would specify the exact shape of the house outline. However, so far I can't see anything in the PBF file that confirms my guess.</p>
<p>TIA, Roger</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-outlines" rel="tag" title="see questions tagged &#39;outlines&#39;">outlines</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Sep '15, 00:25</strong></p>
<img src="https://secure.gravatar.com/avatar/b44d7798a9612803956406cbc311c124?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mirage&#39;s gravatar image" />
<p><span>Mirage</span><br />
<span class="score" title="39 reputation points">39</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mirage has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Sep '15, 19:49</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45496" class="comments-container">
<span id="45498"></span>
<div id="comment-45498" class="comment">
<div id="post-45498-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Could you amend your question with a description of what data you downloaded and how you filtered it? Perhaps there is something wrong with the process.</p>
</div>
<div id="comment-45498-info" class="comment-info">
<span class="comment-age">(22 Sep '15, 01:23)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45496" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45496-form-container" class="comment-form-container">
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

<span id="45499"></span>

<div id="answer-container-45499" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45499-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45499-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-45499-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your process is, lets say, overly complex.</p>
<p>First read up on the OSM data model <a href="https://wiki.openstreetmap.org/wiki/Elements">https://wiki.openstreetmap.org/wiki/Elements</a> and other pages (it helps to know what you are looking for before you start looking).</p>
<p>Then get a metro extract from <a href="https://mapzen.com/data/metro-extracts">https://mapzen.com/data/metro-extracts</a> or a state level extract. In general it is easier to first pair down size/area of an extract before doing anything else. Then use for example osmfilter (<a href="https://wiki.openstreetmap.org/wiki/Osmfilter)">https://wiki.openstreetmap.org/wiki/Osmfilter)</a> to extract the nodes and ways for the building outlines (you will need to convert to standard XML format first). You are looking for ways that have a building tag.</p>
<p>Note after this process you will have a file containing nodes and ways, no already built geometries.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '15, 08:32</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-45499" class="comments-container">
<span id="45501"></span>
<div id="comment-45501" class="comment">
<div id="post-45501-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Some elements of your suggestion are exactly what I <em>don't</em> want to do. Mainly I don't want to work with XML at all, partially because it's hugely inefficient, and partially because I loath it and think it's one of the worst file formats to ever be foisted on the world of programmers.</p>
<p>However, you do answer the core of my question, for which I'm truly grateful. So it is pretty much as I expected, now I just have to trace the migration of the building tagged ways from the original PBF file to the final state way file and determine where data was lost.</p>
<p>I won't go into my reasons for creating this, in your words, "overly complex" approach, let's just say that I needed to do all these steps anyway, so it didn't seem overly complex to me.</p>
<p>BTW, I did read the <a href="https://wiki.openstreetmap.org/wiki/Elements">https://wiki.openstreetmap.org/wiki/Elements</a> pages, but reading and being sure that you understand what every element is truly representing are different things entirely.</p>
<p>Thanks again for your answer.</p>
</div>
<div id="comment-45501-info" class="comment-info">
<span class="comment-age">(22 Sep '15, 09:49)</span> <span class="comment-user userinfo">Mirage</span>
</div>
</div>
<span id="45503"></span>
<div id="comment-45503" class="comment">
<div id="post-45503-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You don't need to use XML for osmfilter; you can use .o5m instead.</p>
</div>
<div id="comment-45503-info" class="comment-info">
<span class="comment-age">(22 Sep '15, 10:08)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="45504"></span>
<div id="comment-45504" class="comment">
<div id="post-45504-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Working with a small XML file is far faster than trying to prune down the planet, but extracts are available as PBFs too, and osmfilter, osmconvert, and osmosis all work fine with them.</p>
<p>If, starting from an extract, you still have problems, you could post a new question, including the command lines.</p>
</div>
<div id="comment-45504-info" class="comment-info">
<span class="comment-age">(22 Sep '15, 10:26)</span> <span class="comment-user userinfo">pnorman</span>
</div>
</div>
<span id="45506"></span>
<div id="comment-45506" class="comment">
<div id="post-45506-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>XML may be ugly but you can easily do a "grep building myfile.osm" and you'd probably have saved yourself a lot of time (and maybe wouldn't even have had to ask this question). It is not the worst idea to start with XML when you do something with OSM, and upgrade to an efficient format like PBF later - for easier debugging.</p>
</div>
<div id="comment-45506-info" class="comment-info">
<span class="comment-age">(22 Sep '15, 10:57)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="45507"></span>
<div id="comment-45507" class="comment not_top_scorer">
<div id="post-45507-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for all the help, after a small fix here is my first trivial render of Forest Knolls in San Francisco. So now I have house outlines. Now just need to work on OpenGL rendering so it will all look pretty.</p>
<p><span><img src="/upfiles/FirstForestKnollsMap.JPG" alt="house outlines" /></span></p>
</div>
<div id="comment-45507-info" class="comment-info">
<span class="comment-age">(22 Sep '15, 12:48)</span> <span class="comment-user userinfo">Mirage</span>
</div>
</div>
<span id="45508"></span>
<div id="comment-45508" class="comment not_top_scorer">
<div id="post-45508-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Was it a bug in your code or another issue? Maybe you can shed some light for others running into the same problem.</p>
</div>
<div id="comment-45508-info" class="comment-info">
<span class="comment-age">(22 Sep '15, 13:43)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="45516"></span>
<div id="comment-45516" class="comment">
<div id="post-45516-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yeah, it was a bug in my code, so probably not much help for others. I made a stupid error where in one pass I was attempting to grab node data from one of my HashMaps, but rather than looking up each way's indexed node Id in my HashMap, I looked up the index itself in my HashMap. Looking up a "for" loop index in my HashMap is basically a meaningless operation, so everything that happened from there forward was just garbage. Almost surprising that the program didn't just crash. I'm not sure if this is an indication that I write good fault tolerant code, or that I write bad code that helps hide actual bugs.</p>
</div>
<div id="comment-45516-info" class="comment-info">
<span class="comment-age">(23 Sep '15, 03:59)</span> <span class="comment-user userinfo">Mirage</span>
</div>
</div>
</div>
<div id="comment-tools-45499" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-45499-form-container" class="comment-form-container">
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

