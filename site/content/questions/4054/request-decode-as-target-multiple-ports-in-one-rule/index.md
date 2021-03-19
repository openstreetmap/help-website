+++
type = "question"
title = "Request: Decode as - target multiple ports in one rule"
description = '''The use of serial to IP servers is prevalent in the SCADA world. These devices usually set up a single port per serial connection, generally in continuous blocks. The number of ports can range from 1 to 64 (possibly more but I haven&#x27;t seen one yet). It would be useful to be able to set up a dissecto...'''
date = "2011-05-12T10:06:00Z"
lastmod = "2012-10-12T02:36:00Z"
weight = 4054
keywords = [ "decode", "dissector", "request" ]
aliases = [ "/questions/4054" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Request: Decode as - target multiple ports in one rule](/questions/4054/request-decode-as-target-multiple-ports-in-one-rule)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4054-score" class="post-score" title="current number of votes">0</div><span id="post-4054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The use of serial to IP servers is prevalent in the SCADA world. These devices usually set up a single port per serial connection, generally in continuous blocks. The number of ports can range from 1 to 64 (possibly more but I haven't seen one yet).</p><p>It would be useful to be able to set up a dissector override that targets a port range. Currently you have to set up each port manually and Wireshark forgets the settings when you shut it down.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '11, 10:06</strong></p><img src="https://secure.gravatar.com/avatar/e02fcbac42180de96eeb73c80b6faa33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Graemem&#39;s gravatar image" /><p><span>Graemem</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Graemem has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 May '11, 11:15</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-4054" class="comments-container"></div><div id="comment-tools-4054" class="comment-tools"></div><div class="clear"></div><div id="comment-4054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="4059"></span>

<div id="answer-container-4059" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4059-score" class="post-score" title="current number of votes">0</div><span id="post-4059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="http://ask.wireshark.org/users/655/jeffmorriss/">Jeff</a>'s answer to the <a href="http://ask.wireshark.org/questions/4053/request-decode-as-save-and-load-settings">Request: Decode as - save and load settings</a> question.</p><p>Basically, "range" preferences can be used to do this for the dissectors in question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 May '11, 11:25</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Dec '11, 06:53</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-4059" class="comments-container"><span id="14928"></span><div id="comment-14928" class="comment"><div id="post-14928-score" class="comment-score"></div><div class="comment-text"><p>Where can I find the "range" prefences for a dissector?</p></div><div id="comment-14928-info" class="comment-info"><span class="comment-age">(11 Oct '12, 06:49)</span> <span class="comment-user userinfo">Graemem</span></div></div><span id="14932"></span><div id="comment-14932" class="comment"><div id="post-14932-score" class="comment-score"></div><div class="comment-text"><p>See the prefs_register_range_preference() function. For an example using that function, look at the Diameter dissector (epan/dissectors/packet-diameter.c).</p></div><div id="comment-14932-info" class="comment-info"><span class="comment-age">(11 Oct '12, 08:35)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-4059" class="comment-tools"></div><div class="clear"></div><div id="comment-4059-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14929"></span>

<div id="answer-container-14929" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14929-score" class="post-score" title="current number of votes">0</div><span id="post-14929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Currently you have to set up each port manually and <strong>Wireshark forgets the settings</strong> when you shut it down.</p></blockquote><p>In the dialog "Decode as" select the protocol and click on <strong>Apply</strong>. Then click on the button "Show Current" and click on <strong>save</strong>. Wireshark will then remember these settings.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '12, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Oct '12, 07:08</strong> </span></p></div></div><div id="comments-container-14929" class="comments-container"></div><div id="comment-tools-14929" class="comment-tools"></div><div class="clear"></div><div id="comment-14929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14953"></span>

<div id="answer-container-14953" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14953-score" class="post-score" title="current number of votes">0</div><span id="post-14953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have found a solution!</p><p>The save User Specified Decodes has a bug. I am using 120 sockets in order to manage communications to 40 base stations. After about 20 minutes of manually setting a Decode As for each port I realised that I was seeing previously set ports. Scanning back through the capture file there were chunks of previously set decodes redirections not being applied. If you save more than around 60 entries it will overwrite a previous setting.</p><p>But there is a workaround.</p><p>The User Specified Decodes are kept in a text file in the current profile folder.</p><p>See <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChWindowsFolder.html">http://www.wireshark.org/docs/wsug-html-chunked/ChWindowsFolder.html</a> for the location of the folder.</p><p>The file called "decode-as-entries" contains lines looking like this for DNP3: "decode-as-entry: tcp.port,20031,(none),DNP 3.0"</p><p>I then used a spread sheet to generate the 120 lines of decodes (just to make things fun they are not consequtive), saved it as a csv file, opened it in notepad and copied it into the decode-as-entries file. And it works; all 120 decode redirections are now correctly decoded, and Wireshark remembers the settings after a restart. Also as the decodes are kept in a text file it is easy to transfer them to another PC.</p><p>Note: replace the '-'s with underscores.</p><p>Thanks to all who replied, it really helped.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '12, 01:27</strong></p><img src="https://secure.gravatar.com/avatar/e02fcbac42180de96eeb73c80b6faa33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Graemem&#39;s gravatar image" /><p><span>Graemem</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Graemem has no accepted answers">0%</span></p></div></div><div id="comments-container-14953" class="comments-container"><span id="14954"></span><div id="comment-14954" class="comment"><div id="post-14954-score" class="comment-score"></div><div class="comment-text"><p>Note that as of r44486, I modified the DNP3 dissector to act as a heuristic dissector so that you wouldn't need to use "Decode As" for DNP3 as it should all work automagically.</p><p>This change is only in the 1.9 dev branch at the moment so you'll need to either build from source, or use a nightly build to see the effects. Feedback would be appreciated.</p></div><div id="comment-14954-info" class="comment-info"><span class="comment-age">(12 Oct '12, 01:36)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="14956"></span><div id="comment-14956" class="comment"><div id="post-14956-score" class="comment-score"></div><div class="comment-text"><p>grahamb</p><p>I have tried 1.9.0 r45495 on a 32bit XP pro machine. I can confirm that it looks like it works. I did get some funny decodes so I checked the preferences. They went away when I checked "Protocols, TCP, Try heuristic sub-dissectors first:".</p><p>One difference. I am using 1.8.2 r44520 and I get 55552 packets displayed (dnp3 and not tcp.analysis.retransmission), With the same file and filter on the 1.9.0 v45495 I get 56121 packets marked.</p><p>When I get time I will try to work out what the difference is.</p></div><div id="comment-14956-info" class="comment-info"><span class="comment-age">(12 Oct '12, 02:36)</span> <span class="comment-user userinfo">Graemem</span></div></div></div><div id="comment-tools-14953" class="comment-tools"></div><div class="clear"></div><div id="comment-14953-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

