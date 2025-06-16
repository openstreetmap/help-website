+++
type = "question"
title = "Wrong Error report in JOSM&#x27;s Validation (?)"
description = '''Hi, I&#x27;m a user of JOSM, not a develloper. I have ask similar questions in the Dutch user forum, but only got replies like : &quot;Yep, the validation in JOSM might not be optimal&quot; I&#x27;m a user and editor of the recreational cycle network in The Netherlands and it can cost me considerable time to figure out...'''
date = "2014-05-05T20:42:00Z"
lastmod = "2014-05-07T20:54:00Z"
weight = 32885
keywords = [ "role", "route", "validator", "relation", "josm" ]
aliases = [ "/questions/32885" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wrong Error report in JOSM's Validation (?)](/questions/32885/wrong-error-report-in-josms-validation)

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
<span id="post-32885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32885-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm a user of JOSM, not a develloper. I have ask similar questions in the Dutch user forum, but only got replies like : "Yep, the validation in JOSM might not be optimal"</p>
<p>I'm a user and editor of the recreational cycle network in The Netherlands and it can cost me considerable time to figure out what's wrong with network relations. Especially so when infact the error report is the only thing that's wrong :(</p>
<p>Here is one of many examples :</p>
<p>network=rcn note=23-62 route=bicycle type=route Relation ID=<a href="https://www.openstreetmap.org/relation/1263377#map=16/51.6589/5.2782">1263377</a></p>
<p>JOSM 7000 Validation : Role forward unknown Role backward unknown</p>
<p><a href="http://ra.osmsurround.org/">http://ra.osmsurround.org/</a></p>
<p>Great! This relation seems ok. This relation can be connected as one piece.</p>
<p>Rating The relation analyzer (RA) tries to assemble the relation data to see if it is in one piece (either a line with just two ends, or Y-shaped, or more complicated). The pieces are assembled using rules which include looking at roles such as "forward" and "backward". If a relation cannot be connected into one single piece, the RA will create more than one.</p>
<p>Can someone enlight me please ?</p>
<p>Gys</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-role" rel="tag" title="see questions tagged &#39;role&#39;">role</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-validator" rel="tag" title="see questions tagged &#39;validator&#39;">validator</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 May '14, 20:42</strong></p>
<img src="https://secure.gravatar.com/avatar/5c3b258ebdc5943f1ab6008f146e7f7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gys%20de%20Jongh&#39;s gravatar image" />
<p><span>Gys de Jongh</span><br />
<span class="score" title="713 reputation points">713</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gys de Jongh has 5 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 May '14, 01:20</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-32885" class="comments-container">
<span id="32918"></span>
<div id="comment-32918" class="comment">
<div id="post-32918-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>User SomeOneElse (Andy) mailed two very useful links. I copied them below to clarify a few points.</p>
<p>The route looks like two letters Y joined together :</p>
<p><a href="https://www.openstreetmap.org/relation/1263377#map=17/51.66097/5.28077&amp;layers=CN">https://www.openstreetmap.org/relation/1263377#map=17/51.66097/5.28077&amp;layers=CN</a></p>
<p>It might look odd but Imo this is a combination of 3 factors :</p>
<p>1) The elaborate cycle infra structure in The Netherlands. For our local hero have a look at this blog : <a href="http://bicycledutch.wordpress.com/">http://bicycledutch.wordpress.com/</a></p>
<p>The two branches of the top Y are two completely separate bicycle tracks along a motorway. Same for the two branches of the lower Y.</p>
<p>This piece :</p>
<p><a href="https://www.openstreetmap.org/relation/1263377#map=17/51.66097/5.28077&amp;layers=CN">https://www.openstreetmap.org/relation/1263377#map=17/51.66097/5.28077&amp;layers=CN</a></p>
<p>has no attached role is an old village road with no separate bicycle tracks. The cycle route uses this piece both to travel from 23 to 62 as well as to travel from 62 to 23</p>
<p>2) The actual route made by the people who maintain them. Which is apparent from the little whight/green cycle node signs. The little piece with the backward role is not a oneway road. It connects the residential road with the roundabout. You could travel in the other direction then the direction in which the road was drawn. Meaning you won't get trouble with the police. But the people who maintain the network decided that you should only use that piece opposite to the direction it was drawn.</p>
<p>3) In which case Osm wants the role to be "backward" or I could change the direction of drawing of that piece of road to stop JOSM from cying "wolf" But that is not recommended and feels like tagging for the renderer.</p>
<p>If you zoom a bit further on the link to the relation than you will see that the top Y ends in two rcn_ref=23 and the lower Y ends in two rcn_ref=62 . Both rcn_ref=23 and rcn_ref=62 are just on the left and right side of the road.</p>
<p>The physical situation for both is a motorway with two completely separate bicyle tracks. So the two nodes rcn_ref=62 are maybe 20 meters apart. Same for rcn_ref=23. In that case the recommende solution is two nodes with the same number in stead of painstakingly splitting up to connect the cycletrack for 23-62 with the cycle track for 62-23</p>
<p>So, I really don't see anything wrong.</p>
<p>The relation is continuous now. It was not before. This actually is the reason I edited it. I must have travalled this route by bike a few hundred times at least, so I know the situation. JOSM validation can generate a "not continuous error" but it nolonger does so.</p>
<p>The "wrong role" error in the JOSM validator can be selected while you have the relation editor open, but nothing is highligted there. On the map the whole relation is highligted. Not very helpfull :(</p>
<p>Gys</p>
</div>
<div id="comment-32918-info" class="comment-info">
<span class="comment-age">(06 May '14, 21:17)</span> <span class="comment-user userinfo">Gys de Jongh</span>
</div>
</div>
<span id="32920"></span>
<div id="comment-32920" class="comment">
<div id="post-32920-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If I use this</p>
<p><a href="http://yournavigation.org/index.php">http://yournavigation.org/index.php</a></p>
<p>service and zoom in maximally then the shortes bicycle route from the western rcn_ref=23 to the western rcn_ref=62 is drawn completely as intended by the maintainers of the cycle network.</p>
<p>The shortes bicycle route from eastern rcn_ref=62 to the eastern rcn_ref=23 is drawn as intended by the maintainers of the cycle network if I add one extra waypoint in the first roudabout junction Postweg/Loonsebaan. If I leave this extra waypoint out then then the calculated route follows this roundabout junction in the other direction. Which is both legal and possible but not as intended by the maintainers of the cycle network.</p>
<p>Again the route relation seems perfectly Ok</p>
</div>
<div id="comment-32920-info" class="comment-info">
<span class="comment-age">(06 May '14, 21:18)</span> <span class="comment-user userinfo">Gys de Jongh</span>
</div>
</div>
<span id="32922"></span>
<div id="comment-32922" class="comment not_top_scorer">
<div id="post-32922-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>sorry, Gys, you are <span>wrong</span> in this help site. Please discuss such specific problems <span>elsewhere</span> - eg. in the <a href="http://forum.openstreetmap.org/">forum</a>.</p>
</div>
<div id="comment-32922-info" class="comment-info">
<span class="comment-age">(07 May '14, 01:28)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="32923"></span>
<div id="comment-32923" class="comment">
<div id="post-32923-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><span>@aseerel4c26</span> Er, what? Asking how JOSM picks up rules for different relation types seems to me exactly on-topic for this help site. As mentioned above, this question was previously asked in the forum (and also on the newbies list), so sending the user back there is unlikely to help.</p>
</div>
<div id="comment-32923-info" class="comment-info">
<span class="comment-age">(07 May '14, 01:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="32926"></span>
<div id="comment-32926" class="comment not_top_scorer">
<div id="post-32926-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@SomeoneElse</span>: I think a forum is exactly the best place for the specific problem. By the way: no forum link to the first post given. :-( What can be said in general, is in my answer below ... but the question (and "comments" - which were "answers" too) is much too specific for this site. You notice it already by the use of the "answer" function for a additional comments (which are TL;DR).</p>
<p>Oh, and if the question is "how JOSM picks up rules for different relation types", then it has the wrong title.</p>
</div>
<div id="comment-32926-info" class="comment-info">
<span class="comment-age">(07 May '14, 01:43)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="32930"></span>
<div id="comment-32930" class="comment">
<div id="post-32930-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><span>@aseerel4c26</span>: Congrats you just restored my trust in humanity. In any forum there will always be a helpful guy who replies that this is the wrong forum or points to a spelling error. Godwins Law Thanks</p>
</div>
<div id="comment-32930-info" class="comment-info">
<span class="comment-age">(07 May '14, 07:47)</span> <span class="comment-user userinfo">Gys de Jongh</span>
</div>
</div>
<span id="32933"></span>
<div id="comment-32933" class="comment not_top_scorer">
<div id="post-32933-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@aseerel4c26</span> If you think the comments are Tl;Dr have JOSM check your attention span and go back to Imgur</p>
</div>
<div id="comment-32933-info" class="comment-info">
<span class="comment-age">(07 May '14, 08:06)</span> <span class="comment-user userinfo">Gys de Jongh</span>
</div>
</div>
<span id="32938"></span>
<div id="comment-32938" class="comment not_top_scorer">
<div id="post-32938-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@Gys de Jongh</span>: is there any need for those personal attacks? Please ...</p>
</div>
<div id="comment-32938-info" class="comment-info">
<span class="comment-age">(07 May '14, 13:46)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="32941"></span>
<div id="comment-32941" class="comment">
<div id="post-32941-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Good question, on an issue which has been bugging quite a lot of us without any resolution. Thanks for raising it and getting us just a little further on the way to resolving the issue.</p>
</div>
<div id="comment-32941-info" class="comment-info">
<span class="comment-age">(07 May '14, 18:12)</span> <span class="comment-user userinfo">Frankl2009</span>
</div>
</div>
</div>
<div id="comment-tools-32885" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-32885-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="32928"></span>

<div id="answer-container-32928" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32928-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-32928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's a bug in the JOSM validator, I think. For <code>item name="Bicycle route"</code> <code>"data/defaultpresets.xml"</code> contains:</p>
<pre><code>        &lt;roles&gt;
            &lt;role key=&quot;&quot; text=&quot;route segment&quot; requisite=&quot;required&quot; type=&quot;way&quot;/&gt;
        &lt;/roles&gt;</code></pre>
<p>whereas for <code>item name="Piste route"</code> it contains:</p>
<pre><code>        &lt;roles&gt;
           &lt;role key=&quot;&quot; text=&quot;route segment&quot; requisite=&quot;optional&quot; type=&quot;way&quot; /&gt;
            &lt;role key=&quot;forward&quot; text=&quot;forward segment&quot; requisite=&quot;optional&quot; type=&quot;way&quot; /&gt;
            &lt;role key=&quot;backward&quot; text=&quot;backward segment&quot; requisite=&quot;optional&quot; type=&quot;way&quot; /&gt;
            &lt;role key=&quot;link&quot; text=&quot;link segment&quot; requisite=&quot;optional&quot; type=&quot;way&quot; /&gt;
            &lt;role key=&quot;shortcut&quot; text=&quot;shortcut segment&quot; requisite=&quot;optional&quot; type=&quot;way&quot; /&gt;
            &lt;role key=&quot;variant&quot; text=&quot;variant segment&quot; requisite=&quot;optional&quot; type=&quot;way&quot; /&gt;
            &lt;role key=&quot;start&quot; text=&quot;entry points&quot; requisite=&quot;optional&quot; type=&quot;node&quot; /&gt;
        &lt;/roles&gt;</code></pre>
<p>I can see no logical reason why a bicycle route way can't be oneway.</p>
<p>A similar symptom was reported <a href="http://josm.openstreetmap.de/ticket/8266">here</a> (although that looks like it wasn't actually a bug as such - it was due to a confusion of the "new" and "old" public transport schemas).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 May '14, 03:16</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-32928" class="comments-container">
<span id="32932"></span>
<div id="comment-32932" class="comment">
<div id="post-32932-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Andy, Imo you traced down the error in JOSM's validator. This will be most helpful for The Netherlands. We have a very dense cycle network which is becomming almost impossible to maintain because about 30% of the routes are polluted with JOSM validator errors. I will post a link on the forum here : <a href="http://forum.openstreetmap.org/viewforum.php?id=12">http://forum.openstreetmap.org/viewforum.php?id=12</a></p>
<p>Thanks again Gys</p>
</div>
<div id="comment-32932-info" class="comment-info">
<span class="comment-age">(07 May '14, 07:59)</span> <span class="comment-user userinfo">Gys de Jongh</span>
</div>
</div>
<span id="32935"></span>
<div id="comment-32935" class="comment">
<div id="post-32935-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>JOSM developers are very unlikely to notice complaints on the Dutch forum and only slightly more likely to notice problems reported here. So I create a bug report for this issue: <a href="http://josm.openstreetmap.de/ticket/9992">http://josm.openstreetmap.de/ticket/9992</a></p>
</div>
<div id="comment-32935-info" class="comment-info">
<span class="comment-age">(07 May '14, 11:21)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="32936"></span>
<div id="comment-32936" class="comment">
<div id="post-32936-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Gys, for maintaining the cycle and walking networks in Belgium and The Netherlands, you're better off with e.g. <a href="http://osma.vmarc.be/">http://osma.vmarc.be/</a> which has specialized tests and knowledge about those type of networks.</p>
</div>
<div id="comment-32936-info" class="comment-info">
<span class="comment-age">(07 May '14, 12:34)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="32942"></span>
<div id="comment-32942" class="comment">
<div id="post-32942-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks escada, I find myself frequently looking at this : <a href="http://osma.vmarc.be/en/network/1061480">http://osma.vmarc.be/en/network/1061480</a> because it's in my back yard. Note the frustrating numbers of "Errors" I would like to get rid of all of them :(</p>
</div>
<div id="comment-32942-info" class="comment-info">
<span class="comment-age">(07 May '14, 20:32)</span> <span class="comment-user userinfo">Gys de Jongh</span>
</div>
</div>
<span id="32944"></span>
<div id="comment-32944" class="comment">
<div id="post-32944-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@cartinus</span> thanks a lot ! I don't know what you did, but to me it sounds like exactly what I would have liked to do : wake up the programmers to improver their error checking in JOSM :)</p>
<p>Thanks again Gys</p>
</div>
<div id="comment-32944-info" class="comment-info">
<span class="comment-age">(07 May '14, 20:42)</span> <span class="comment-user userinfo">Gys de Jongh</span>
</div>
</div>
</div>
<div id="comment-tools-32928" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32928-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32924"></span>

<div id="answer-container-32924" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32924-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general, <span>JOSM's validator</span> is just a tool like <span>many others</span> which <em>might</em> help you to spot problems in the data. It <em>may have false positives</em>. JOSM's validator has different issue classes (error, warning, info) which show you the severity of the shown issue and – IMHO – correlate with false positive error rate. Such tools are never 100 % right.</p>
<p>Regarding the validator's warning about relation member roles also see the <em>similar</em> (core) problem <a href="/questions/28602/">what-does-the-warning-role-reverse-unknown-role-verification-problem-mean-in-josm</a>.</p>
<p>If you feel that a false positive is a programming error (e.g. a systematic false positive which occurs very often which was not shown in the older versions) or if there are many false positives which could be easily avoided, please report to the programmers of JOSM (bug tracker, see first link).</p>
<p>Also see my comment above for other discussion places.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 May '14, 01:37</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 May '14, 02:03</strong> </span></p>
</div>
</div>
<div id="comments-container-32924" class="comments-container">
<span id="32931"></span>
<div id="comment-32931" class="comment">
<div id="post-32931-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@aseerel4c26</span>: If a tool bites you it's a bug and as I told you 1) I'm not a programmer of JOSM just a user 2)I posted this on several fora already</p>
</div>
<div id="comment-32931-info" class="comment-info">
<span class="comment-age">(07 May '14, 07:53)</span> <span class="comment-user userinfo">Gys de Jongh</span>
</div>
</div>
<span id="32937"></span>
<div id="comment-32937" class="comment">
<div id="post-32937-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@Gys de Jongh</span>: Sure, I read that you are no programmer but I told you how to report it to the programmers. Programmers depend on feedback and bugreports of the users. It seems you missed this. In the meantime, Cartinus has reported it there (see his comment above).</p>
</div>
<div id="comment-32937-info" class="comment-info">
<span class="comment-age">(07 May '14, 13:45)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="32943"></span>
<div id="comment-32943" class="comment">
<div id="post-32943-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@aseerel4c26</span> Can you please fire your other brain cell ? What do you think I'm doing ? I started this thread by saying that I'm not a programmer and want to provide feedback to the guys who devellop JOSM and posted this at the appropriate sites.</p>
</div>
<div id="comment-32943-info" class="comment-info">
<span class="comment-age">(07 May '14, 20:36)</span> <span class="comment-user userinfo">Gys de Jongh</span>
</div>
</div>
<span id="32945"></span>
<div id="comment-32945" class="comment">
<div id="post-32945-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Gys de Jongh</span>: unbelievable, I hope someone soon deletes your comment (this one then too, of course).</p>
</div>
<div id="comment-32945-info" class="comment-info">
<span class="comment-age">(07 May '14, 20:54)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-32924" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32924-form-container" class="comment-form-container">
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

