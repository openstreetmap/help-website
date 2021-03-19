+++
type = "question"
title = "1.12.4 hangs on Ubuntu after install"
description = '''Hi, I dl the latest Wireshark 1.12.4 source and compiled under latest Ubuntu. My setup: ./configure --prefix=/usr --with-gtk2=yes --with-gtk3=no --without-qt --sysconfdir=/etc --with-lua=no The long compilation went ok (after few minor -l fixes..) and when I run the wrapping script from build dir ./...'''
date = "2015-05-08T01:44:00Z"
lastmod = "2015-05-08T14:51:00Z"
weight = 42201
keywords = [ "hangs", "bug", "install" ]
aliases = [ "/questions/42201" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [1.12.4 hangs on Ubuntu after install](/questions/42201/1124-hangs-on-ubuntu-after-install)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42201-score" class="post-score" title="current number of votes">0</div><span id="post-42201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,<br />
I dl the latest Wireshark 1.12.4 source and compiled under latest Ubuntu.<br />
My setup:<br />
./configure --prefix=/usr --with-gtk2=yes --with-gtk3=no --without-qt --sysconfdir=/etc --with-lua=no</p><p>The long compilation went ok (after few minor -l fixes..) and when I run the wrapping script from build dir ./wireshark, the program opens and runs OK allright.<br />
</p><p>Then, I run "make install", no errors, and I can run wireshark from path.<br />
<strong>BUT</strong>, it hangs, forever in a loop with high CPU.<br />
Here the strace log:<br />
[...]<br />
clock_gettime(CLOCK_MONOTONIC, {391, 42624826}) = 0<br />
recvmsg(3, 0xbff3ec14, 0) = -1 EAGAIN (Resource temporarily unavailable)<br />
clock_gettime(CLOCK_MONOTONIC, {391, 43554457}) = 0<br />
poll([{fd=4, events=POLLIN}, {fd=3, events=POLLIN}, {fd=5, events=POLLIN}], 3, 23) = 0 (Timeout)<br />
clock_gettime(CLOCK_MONOTONIC, {391, 67730651}) = 0<br />
recvmsg(3, 0xbff3ec14, 0) = -1 EAGAIN (Resource temporarily unavailable)<br />
clock_gettime(CLOCK_MONOTONIC, {391, 68576702}) = 0<br />
poll([{fd=4, events=POLLIN}, {fd=3, events=POLLIN}, {fd=5, events=POLLIN}], 3, 75) = 0 (Timeout)<br />
clock_gettime(CLOCK_MONOTONIC, {391, 145234474}) = 0<br />
recvmsg(3, 0xbff3ec14, 0) = -1 EAGAIN (Resource temporarily unavailable)<br />
[...]<br />
</p><p>Any help??</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hangs" rel="tag" title="see questions tagged &#39;hangs&#39;">hangs</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '15, 01:44</strong></p><img src="https://secure.gravatar.com/avatar/054a5bf4cea5a2e02665f19ce9dde42a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nikita&#39;s gravatar image" /><p><span>nikita</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nikita has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 May '15, 01:45</strong> </span></p></div></div><div id="comments-container-42201" class="comments-container"><span id="42204"></span><div id="comment-42204" class="comment"><div id="post-42204-score" class="comment-score"></div><div class="comment-text"><p>did you run sudo ldconfig after install? Logging off and back on might make a difference too.</p></div><div id="comment-42204-info" class="comment-info"><span class="comment-age">(08 May '15, 03:35)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="42208"></span><div id="comment-42208" class="comment"><div id="post-42208-score" class="comment-score"></div><div class="comment-text"><p>yes I did, it still hangs.<br />
Can anybody explain me the meaning of those messages in the strace log?<br />
If I could understand what those strace messages mean, I can try debug further myself the issue.<br />
Thanks</p></div><div id="comment-42208-info" class="comment-info"><span class="comment-age">(08 May '15, 04:11)</span> <span class="comment-user userinfo">nikita</span></div></div><span id="42209"></span><div id="comment-42209" class="comment"><div id="post-42209-score" class="comment-score"></div><div class="comment-text"><p>Note the OP is using Utopic (14.10) which is EOL in July 2015.</p><p>What were the "few minor -l fixes.."?</p></div><div id="comment-42209-info" class="comment-info"><span class="comment-age">(08 May '15, 04:13)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="42210"></span><div id="comment-42210" class="comment"><div id="post-42210-score" class="comment-score"></div><div class="comment-text"><p>actually, I was sarcastic, I had to add lots of libs, X and common ones into configure AND makefile, it took <strong>forever</strong> to compile and make it work... but finally it worked... and, as I wrote, when I run the wrapping script from build dir (./wireshark or .libs/lt-wireshark),it works ok...<br />
the problem I repeat, is <strong>after</strong> make install.<br />
Any help with those strace msg?</p></div><div id="comment-42210-info" class="comment-info"><span class="comment-age">(08 May '15, 04:40)</span> <span class="comment-user userinfo">nikita</span></div></div><span id="42211"></span><div id="comment-42211" class="comment"><div id="post-42211-score" class="comment-score"></div><div class="comment-text"><p>Apparently after all your changes it doesn't work. Can you possibly try CMake instead of autotools?</p><p>Either way it might be helpful to post the configure logs somewhere for inspection. I know the problem seems to be only after install, but as your system seems to have issues configuring and building let's start there.</p></div><div id="comment-42211-info" class="comment-info"><span class="comment-age">(08 May '15, 04:47)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="42212"></span><div id="comment-42212" class="comment not_top_scorer"><div id="post-42212-score" class="comment-score"></div><div class="comment-text"><p>On another note, have you looked at installing the wireshark-dev package from the repository? Yes, it says 1.12.1+g01b65bf-2~ubuntu14.10.3, but that would have gotten you close enough.</p></div><div id="comment-42212-info" class="comment-info"><span class="comment-age">(08 May '15, 06:36)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="42214"></span><div id="comment-42214" class="comment not_top_scorer"><div id="post-42214-score" class="comment-score"></div><div class="comment-text"><p>it is the first time I try compile Wireshark from source code,I really don't want to do it anymore... :P<br />
Basically I googled around, and found out that the source of all issues is goddamn GTK3, so it is needed and recompile Wireshark with GTK2 only (leave qt out).<br />
Well, It is true, with GTK2 all works good.<br />
So, btw, I don't really understand why cursing ourselves with that mess GTK3 (and why there are deb packages for GTK3, QT, but not for GTK2?!?)<br />
Anyway, I did my best trying understand what all those configure options do, and that line you read up is the best I could come out with, so I believe there must be a more correct way, isn't it?.<br />
Yes Jaap, I did that.<br />
Yes, grahamb, let me try to remember myself what I did: I added few -l libs which were required, and which were not added by configure, I used gnu standard make, I dl bison and flex, I cut out from the configure script the part of GDK2 test, because it kept asking for more -lXlibs to add(again maybe there was a smarter way by command line option), then in the resulting makefile, I added 10 or smthg more -lLibs to wireshark link, to dumpcap, and a couple of more tools - and basically that's it.<br />
One very important thing I was forced to discover, with the new gcc, the -l options must all go at <strong>end</strong> of gcc command line!<br />
Now I really hope someone can decode the meaning of those strace messages I posted, because I already feel cursed.. ;)</p></div><div id="comment-42214-info" class="comment-info"><span class="comment-age">(08 May '15, 07:43)</span> <span class="comment-user userinfo">nikita</span></div></div><span id="42216"></span><div id="comment-42216" class="comment not_top_scorer"><div id="post-42216-score" class="comment-score"></div><div class="comment-text"><p>To get a build environment on Debian derivatives you can use <code>apt-get build-dep wireshark</code>.</p><p>When I've built on Ubuntu, I've just used the above and then CMake.</p></div><div id="comment-42216-info" class="comment-info"><span class="comment-age">(08 May '15, 08:06)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="42219"></span><div id="comment-42219" class="comment not_top_scorer"><div id="post-42219-score" class="comment-score"></div><div class="comment-text"><p>grahamb, I repeat, the problem is <strong>not</strong> missing build dependency libs!<br />
.libs/lt-wireshark runs ok.<br />
I already have all libs X, GTK2, and so on, all in (only added bison and flex).</p></div><div id="comment-42219-info" class="comment-info"><span class="comment-age">(08 May '15, 08:21)</span> <span class="comment-user userinfo">nikita</span></div></div><span id="42235"></span><div id="comment-42235" class="comment not_top_scorer"><div id="post-42235-score" class="comment-score"></div><div class="comment-text"><p>Which only means that your environment is setup for running Wireshark from its build directory, but not when installed at the system directories. The fact that you apparently need to manually add library references for the linker doesn't bode well here. So what about the raw data? Putting your config.log and strace onto pastbin or alike an option? With just snippets and recollections we're note getting ahead unfortunately. I'm not even sure anyone has a Ubuntu/Utopic platform (or VM) available to work/test with, so the (full) logs will have to do the trick.</p></div><div id="comment-42235-info" class="comment-info"><span class="comment-age">(08 May '15, 14:13)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="42238"></span><div id="comment-42238" class="comment not_top_scorer"><div id="post-42238-score" class="comment-score"></div><div class="comment-text"><p>well Jaap, Im writing here in the hope some Dev from Wireshark team will actually read, and explain what is the meaning of those looped strace messages, e.g. what's that recvmsg 0xbff3ec14, or pool timeout, or anything which can hint where to have a look.<br />
As I said, I'm not gonna recompile anything, that was painful enough, so dunno, what logs can I pastbin foya?<br />
FYI, actually I'm back using the standard pack, as workaround Im saving the load of frames in a pcap under utopic, and then do the analysis under Windows XP where latest Wireshark works as it should (sorry to say, but thats the truth)</p></div><div id="comment-42238-info" class="comment-info"><span class="comment-age">(08 May '15, 14:51)</span> <span class="comment-user userinfo">nikita</span></div></div></div><div id="comment-tools-42201" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-42201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

