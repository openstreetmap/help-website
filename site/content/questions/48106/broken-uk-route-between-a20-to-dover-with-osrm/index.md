+++
type = "question"
title = "[closed] Broken UK route between A20 to Dover with OSRM"
description = '''Hello, We are using our OSRM instance for routing applications and since our last update on 1st Feb we have ran into a routing problem. We have observed a problem on one of our route which were correct before between A20 Archcliffe Road (51.11420, 1.30183) going east 300meters approx to A20 Archclif...'''
date = "2016-02-13T21:40:00Z"
lastmod = "2016-02-14T22:03:00Z"
weight = 48106
keywords = [ "osrm", "routingerror", "tagging", "highway" ]
aliases = [ "/questions/48106" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Broken UK route between A20 to Dover with OSRM](/questions/48106/broken-uk-route-between-a20-to-dover-with-osrm)

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
<span id="post-48106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48106-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>We are using our OSRM instance for routing applications and since our last update on 1st Feb we have ran into a routing problem.</p>
<p>We have observed a problem on one of our route which were correct before between A20 Archcliffe Road (51.11420, 1.30183) going east 300meters approx to A20 Archcliffe Road (51.1146, 1.3043) over a roundabout. This route now goes all round A20 west via B2011 and A256 giving a total route of 12kms.</p>
<p>Please see the link below:</p>
<p><a href="https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=51.1143%2C1.3023%3B51.1146%2C1.3043#map=14/51.1151/1.2765">https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=51.1143%2C1.3023%3B51.1146%2C1.3043#map=14/51.1151/1.2765</a></p>
<p>Using Mapzen the routing works correctly as plotted below:</p>
<p><a href="https://www.openstreetmap.org/directions?engine=mapzen_car&amp;route=51.1143%2C1.3023%3B51.1146%2C1.3043#map=19/51.11449/1.30330">https://www.openstreetmap.org/directions?engine=mapzen_car&amp;route=51.1143%2C1.3023%3B51.1146%2C1.3043#map=19/51.11449/1.30330</a></p>
<p>I have tried to correct this problem on the OpenStreetMap editor by removing a barrier tag which was at the start of this roundabout which looked like a possible cause. But it hasn’t worked and routing is still incorrect for OSRM.</p>
<p>Also, when trying to fix this problem found another.</p>
<p>Generate a straight route from a junction exit on A20 roundabout B2011 (51.10479, 1.24031) to exit of B2011 to A20 (51.10479, 1.24031) and the OSRM routing fails.</p>
<p>The route is blocked at the exit of B2011 round about. So the route generated is very long via Folkestone Road, A256 and back on A20 on other side of the carriage way. Please see the link below:</p>
<p><a href="https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=51.10565%2C1.23703%3B51.10434%2C1.24182#map=14/51.1151/1.2753">https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=51.10565%2C1.23703%3B51.10434%2C1.24182#map=14/51.1151/1.2753</a></p>
<p>If I select the Mapzen routing for the same the correct route is displayed as plotted below:</p>
<p><a href="https://www.openstreetmap.org/directions?engine=mapzen_car&amp;route=51.1057%2C1.2370%3B51.1043%2C1.2418#map=18/51.10501/1.23943">https://www.openstreetmap.org/directions?engine=mapzen_car&amp;route=51.1057%2C1.2370%3B51.1043%2C1.2418#map=18/51.10501/1.23943</a></p>
<p>Can someone please be able to help with this routing problem as these routes are very crucial for our systems.</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-routingerror" rel="tag" title="see questions tagged &#39;routingerror&#39;">routingerror</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Feb '16, 21:40</strong></p>
<img src="https://secure.gravatar.com/avatar/e18ace78200588e4f90bf97cb4ff9810?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kushagra%20Bhargava&#39;s gravatar image" />
<p><span>Kushagra Bha...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kushagra Bhargava has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Feb '16, 21:11</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-48106" class="comments-container">
<span id="48108"></span>
<div id="comment-48108" class="comment not_top_scorer">
<div id="post-48108-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you already tried contacting the OSRM developer(s) via IRC, mailing list, twitter or GitHub?</p>
</div>
<div id="comment-48108-info" class="comment-info">
<span class="comment-age">(13 Feb '16, 22:27)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="48110"></span>
<div id="comment-48110" class="comment not_top_scorer">
<div id="post-48110-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes I have now raised my issues with OSRM developers via IRC, twitter and GitHub. Thanks.</p>
</div>
<div id="comment-48110-info" class="comment-info">
<span class="comment-age">(13 Feb '16, 23:41)</span> <span class="comment-user userinfo">Kushagra Bha...</span>
</div>
</div>
<span id="48111"></span>
<div id="comment-48111" class="comment">
<div id="post-48111-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>the barrier edit was this one <a href="https://www.openstreetmap.org/node/479461452/history">https://www.openstreetmap.org/node/479461452/history</a> , right? <code>barrier=tr</code> seems indeeed strange to me. If it caused a problem - I do not know. In any case, keep in mind that OSRM needs time to update to the new data.</p>
<p>Do you have more questions or can we close this question here? It would be nice if you could link the github issues here.</p>
</div>
<div id="comment-48111-info" class="comment-info">
<span class="comment-age">(14 Feb '16, 00:55)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="48112"></span>
<div id="comment-48112" class="comment not_top_scorer">
<div id="post-48112-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes this was the edit. The barrier=tr was added a month ago. I guess this can be closed here as I have raised this issue with OSRM links mentioned above.</p>
<p>Btw do you know approximately how long does it takes for OSRM to update?</p>
</div>
<div id="comment-48112-info" class="comment-info">
<span class="comment-age">(14 Feb '16, 01:07)</span> <span class="comment-user userinfo">Kushagra Bha...</span>
</div>
</div>
<span id="48113"></span>
<div id="comment-48113" class="comment not_top_scorer">
<div id="post-48113-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, sorry, I do not know (guess: one day up to a month). Please just ask it as a new question entry here if you cannot find it in the old questions.</p>
</div>
<div id="comment-48113-info" class="comment-info">
<span class="comment-age">(14 Feb '16, 01:14)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="48115"></span>
<div id="comment-48115" class="comment">
<div id="post-48115-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It would be nice if you could provide links to the other places where you raised this issue. The GitHub issue is here: <a href="https://github.com/Project-OSRM/osrm-backend/issues/1977">https://github.com/Project-OSRM/osrm-backend/issues/1977</a></p>
</div>
<div id="comment-48115-info" class="comment-info">
<span class="comment-age">(14 Feb '16, 08:53)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="48119"></span>
<div id="comment-48119" class="comment not_top_scorer">
<div id="post-48119-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for copying this link here. That's the main place where I have raised this issue. On twitter I have just posted the tweet with this link.</p>
</div>
<div id="comment-48119-info" class="comment-info">
<span class="comment-age">(14 Feb '16, 12:54)</span> <span class="comment-user userinfo">Kushagra Bha...</span>
</div>
</div>
<span id="48120"></span>
<div id="comment-48120" class="comment">
<div id="post-48120-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Just checked the OSRM and seems like the changes on this route are now updated and it is now working correctly. Thank you all for looking into this matter.</p>
</div>
<div id="comment-48120-info" class="comment-info">
<span class="comment-age">(14 Feb '16, 13:10)</span> <span class="comment-user userinfo">Kushagra Bha...</span>
</div>
</div>
<span id="48125"></span>
<div id="comment-48125" class="comment">
<div id="post-48125-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>OSRM will avoid any barrier which it doesn't understand, so was behaving correctly. I have no idea what barrier=tr was meant to be,</p>
</div>
<div id="comment-48125-info" class="comment-info">
<span class="comment-age">(14 Feb '16, 19:53)</span> <span class="comment-user userinfo">trigpoint</span>
</div>
</div>
<span id="48126"></span>
<div id="comment-48126" class="comment">
<div id="post-48126-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I wrote a message (asking what barrier=tr should mean) to the relevant user on 14 February 2016 at 00:59 but did not get a reply yet.</p>
</div>
<div id="comment-48126-info" class="comment-info">
<span class="comment-age">(14 Feb '16, 19:58)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="48127"></span>
<div id="comment-48127" class="comment not_top_scorer">
<div id="post-48127-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I check on the OSRM but barrier has no value of tr. Mauls a month ago. Not sure though why this barrier field was applied if tr was an invalid value. But surely removing it seems to fixed it. A new highway=traffic_signal tag was added which applies the speed restrictions, doubt that would have made any difference.</p>
</div>
<div id="comment-48127-info" class="comment-info">
<span class="comment-age">(14 Feb '16, 21:44)</span> <span class="comment-user userinfo">Kushagra Bha...</span>
</div>
</div>
<span id="48128"></span>
<div id="comment-48128" class="comment not_top_scorer">
<div id="post-48128-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/11981/kushagra-bhargava">@Kushagra</a> OSM has a quite unrestricted tagging approach. If you think that you do not want to stick to established tag keys/values then you can use <a href="https://wiki.openstreetmap.org/wiki/Any_tags_you_like">any tags you like</a>, hence <code>barrier=tr</code> is not wrong per so ... but it may be not that useful (in fact I guess it is a typing accident).</p>
</div>
<div id="comment-48128-info" class="comment-info">
<span class="comment-age">(14 Feb '16, 22:03)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48106" class="comment-tools">
<span class="comments-showing"> showing 5 of 12 </span> <a href="#" class="show-all-comments-link">show 7 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-48106-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "(data?) issues raised at other places (see comments)" by aseerel4c26 14 Feb '16, 01:15

</div>

</div>

</div>

