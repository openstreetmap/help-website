+++
type = "question"
title = "install wireshark 1.8.3 in ubuntu 12.04"
description = '''To enable capture traffic on multiple interfaces at once, I tried to install wireshark 1.8.3. However, I encountered the following errors:  capture-pcap-util.c:274:1: error: static declaration of ‘pcap_datalink_name_to_val’ follows non-static declaration /usr/local/include/pcap/pcap.h:326:5: note: p...'''
date = "2012-11-08T20:45:00Z"
lastmod = "2012-11-12T23:58:00Z"
weight = 15753
keywords = [ "installation", "wireshark" ]
aliases = [ "/questions/15753" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [install wireshark 1.8.3 in ubuntu 12.04](/questions/15753/install-wireshark-183-in-ubuntu-1204)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15753-score" class="post-score" title="current number of votes">0</div><span id="post-15753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>To enable capture traffic on multiple interfaces at once, I tried to install wireshark 1.8.3. However, I encountered the following errors:</p><p>capture-pcap-util.c:274:1: error: static declaration of ‘pcap_datalink_name_to_val’ follows non-static declaration /usr/local/include/pcap/pcap.h:326:5: note: previous declaration of ‘pcap_datalink_name_to_val’ was here capture-pcap-util.c:289:1: error: static declaration of ‘pcap_datalink_val_to_name’ follows non-static declaration /usr/local/include/pcap/pcap.h:327:13: note: previous declaration of ‘pcap_datalink_val_to_name’ was here</p><p>After doing some search, I found someone can fix it by reinstall libpcap-dev, or the following commands: step 1:rm &amp; rmdir any file in '/usr/include/pcap<em>';'/usr/local/include/pcap</em>'</p><p>step 2:Download libpcap by 'sudo apt-get install libpcap0.8-dev'</p><p>step 3:./autogen.sh in wireshark dir</p><p>step 4:make clean &amp; make &amp; make install</p><p>However, neither is working on ubuntu 12.04/wireshark 1.8.3</p><p>Anyone can help?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '12, 20:45</strong></p><img src="https://secure.gravatar.com/avatar/5d4b0e49653f79a63f4024c3f377f6bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="geneopenflow&#39;s gravatar image" /><p><span>geneopenflow</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="geneopenflow has no accepted answers">0%</span></p></div></div><div id="comments-container-15753" class="comments-container"></div><div id="comment-tools-15753" class="comment-tools"></div><div class="clear"></div><div id="comment-15753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15766"></span>

<div id="answer-container-15766" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15766-score" class="post-score" title="current number of votes">1</div><span id="post-15766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please run this command.</p><blockquote><p><code>apt-get build-dep wireshark</code><br />
</p></blockquote><p>It will install everything that is necessary to build Wireshark on Ubuntu. See also my answer to the following question:</p><blockquote><p><code>http://ask.wireshark.org/questions/11525/autogen-giving-these-errors-what-wrong-am-i-doing</code><br />
</p></blockquote><p>If you want to run Wireshark without root privileges (after you compiled and installed it), please read the answer of the following question:</p><blockquote><p><code>http://ask.wireshark.org/questions/7976/wireshark-setup-linux-for-nonroot-user</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '12, 02:39</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-15766" class="comments-container"><span id="15781"></span><div id="comment-15781" class="comment"><div id="post-15781-score" class="comment-score"></div><div class="comment-text"><p>since wireshark's version in ubuntu repo is ancient, is it still valid to use apt-get build-dep wireshark? coz I wanna install a newest version from source. thanks a lot</p></div><div id="comment-15781-info" class="comment-info"><span class="comment-age">(09 Nov '12, 14:04)</span> <span class="comment-user userinfo">geneopenflow</span></div></div><span id="15782"></span><div id="comment-15782" class="comment"><div id="post-15782-score" class="comment-score"></div><div class="comment-text"><p>'apt-get build-dep wireshark' just installs all libs and tools (the dependencies) that are necessary to build Wireshark. You still need the current sources (either 1.8.3 or the svn tree) to build your version of Wireshark.</p></div><div id="comment-15782-info" class="comment-info"><span class="comment-age">(09 Nov '12, 14:16)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="15783"></span><div id="comment-15783" class="comment"><div id="post-15783-score" class="comment-score"></div><div class="comment-text"><p>thanks, Kurt. However, after I run apt-get build-dep wireshark and make clean, I reconfigure and make the source. the same problems are still there. Any other possibility?</p></div><div id="comment-15783-info" class="comment-info"><span class="comment-age">(09 Nov '12, 17:39)</span> <span class="comment-user userinfo">geneopenflow</span></div></div><span id="15785"></span><div id="comment-15785" class="comment"><div id="post-15785-score" class="comment-score"></div><div class="comment-text"><p>strange, it works out of the box on my Ubuntu 12.04.</p><p>However, if you still get an error messages about the file /usr/<strong>local</strong>/include/pcap/pcap.h, there must be something different/wrong on your system, as I don't have that file and it's not part of libpcap0.8-dev !?!</p><p>If there is really a file pcap.h in /usr/local/include, please post the output of the following commands:</p><blockquote><p><code>dpkg -S /usr/local/include/pcap/pcap.h</code><br />
<code>diff /usr/local/include/pcap/pcap.h /usr/include/pcap/pcap.h</code><br />
</p></blockquote><p>If the file does not exist, can you please delete your wireshark build directory, download the 1.8.3 sources again and to build it from scratch?</p></div><div id="comment-15785-info" class="comment-info"><span class="comment-age">(09 Nov '12, 17:55)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="15803"></span><div id="comment-15803" class="comment"><div id="post-15803-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Kurt. After several operations, I dont have a dir named /usr/local/include/pcap and the error becomes "/usr/include/pcap/pcap.h:327:13: note: previous declaration of ‘pcap_datalink_val_to_name’ was here " So seems I need to delete the wireshark build directory as you suggested. I think it makes sense coz before I build wireshark 1.8.3 I installed wireshark 1.6.2 and then I remove it from the package manager. I highly doute that I do not completely clean the old version. So could you tell me the complete command to delete wireshark build directory? thanks</p></div><div id="comment-15803-info" class="comment-info"><span class="comment-age">(11 Nov '12, 14:51)</span> <span class="comment-user userinfo">geneopenflow</span></div></div><span id="15804"></span><div id="comment-15804" class="comment not_top_scorer"><div id="post-15804-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So could you tell me the complete command to delete wireshark build directory?</p></blockquote><p>well, I suggest to delete the whole source tree and start from scratch. If you extracted the source to /soft/wireshark run the following command to delete everything.</p><blockquote><p><code>rm -rf /soft/wireshark</code></p></blockquote><p>Then extract the source again to /soft/wireshark and run</p><blockquote><p><code>/autogen.sh</code><br />
<code>./configure</code><br />
<code>make</code></p></blockquote></div><div id="comment-15804-info" class="comment-info"><span class="comment-age">(11 Nov '12, 15:30)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="15811"></span><div id="comment-15811" class="comment not_top_scorer"><div id="post-15811-score" class="comment-score"></div><div class="comment-text"><p>thanks kurt. I did so, the same problems: capture-pcap-util.c:274:1: error: static declaration of ‘pcap_datalink_name_to_val’ follows non-static declaration /usr/include/pcap/pcap.h:326:5: note: previous declaration of ‘pcap_datalink_name_to_val’ was here capture-pcap-util.c:289:1: error: static declaration of ‘pcap_datalink_val_to_name’ follows non-static declaration /usr/include/pcap/pcap.h:327:13: note: previous declaration of ‘pcap_datalink_val_to_name’ was here</p></div><div id="comment-15811-info" class="comment-info"><span class="comment-age">(11 Nov '12, 22:58)</span> <span class="comment-user userinfo">geneopenflow</span></div></div><span id="15846"></span><div id="comment-15846" class="comment not_top_scorer"><div id="post-15846-score" class="comment-score"></div><div class="comment-text"><p>Hm.. strange thing, and I have no good idea.</p><p>Let's try the brute force method. Please post the output of the following commands:</p><blockquote><p><code>find / -name pcap.h  | xargs md5sum</code><br />
<code>md5sum capture-pcap-util.c</code></p></blockquote></div><div id="comment-15846-info" class="comment-info"><span class="comment-age">(12 Nov '12, 23:58)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-15766" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-15766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15757"></span>

<div id="answer-container-15757" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15757-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15757-score" class="post-score" title="current number of votes">0</div><span id="post-15757-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You forgot to configure your build on your platform. The offending routine is protected by <code>HAVE_PCAP_DATALINK_NAME_TO_VAL</code>, which should be setup by configure.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '12, 23:29</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></br></p></div></div><div id="comments-container-15757" class="comments-container"><span id="15780"></span><div id="comment-15780" class="comment"><div id="post-15780-score" class="comment-score"></div><div class="comment-text"><p>I did run ./autogen.sh and ./configure before make. anything else I need to configure? thanks</p></div><div id="comment-15780-info" class="comment-info"><span class="comment-age">(09 Nov '12, 14:02)</span> <span class="comment-user userinfo">geneopenflow</span></div></div></div><div id="comment-tools-15757" class="comment-tools"></div><div class="clear"></div><div id="comment-15757-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

