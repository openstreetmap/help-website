+++
type = "question"
title = "wireshark-1.12.0: make is failing even after resolving dependencies(wireshark-iface_monitor.o)"
description = '''Build output: make[2]: Leaving directory `/home/user/Sharan/Softwares/wireshark-1.12.0/ui/cli&#x27; Making all in . make[2]: Entering directory `/home/user/Sharan/Softwares/wireshark-1.12.0&#x27;  CC wireshark-capture-pcap-util-unix.o  CC wireshark-capture-pcap-util.o  CC wireshark-cfile.o  CC wireshark-cfuti...'''
date = "2014-09-02T03:55:00Z"
lastmod = "2014-09-04T05:57:00Z"
weight = 35927
keywords = [ "make", "error", "iface_monitor.c" ]
aliases = [ "/questions/35927" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark-1.12.0: make is failing even after resolving dependencies(wireshark-iface\_monitor.o)](/questions/35927/wireshark-1120-make-is-failing-even-after-resolving-dependencieswireshark-iface_monitoro)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35927-score" class="post-score" title="current number of votes">0</div><span id="post-35927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Build output:</p><pre><code>make[2]: Leaving directory `/home/user/Sharan/Softwares/wireshark-1.12.0/ui/cli&#39;
Making all in .
make[2]: Entering directory `/home/user/Sharan/Softwares/wireshark-1.12.0&#39;
  CC       wireshark-capture-pcap-util-unix.o
  CC       wireshark-capture-pcap-util.o
  CC       wireshark-cfile.o
  CC       wireshark-cfutils.o
  CC       wireshark-clopts_common.o
  CC       wireshark-frame_tvbuff.o
  CC       wireshark-sync_pipe_write.o
  PERL     version.h
Version configuration file version.conf not found.  Using defaults.
version.h unchanged.
  CC       wireshark-version_info.o
  CC       wireshark-capture_ifinfo.o
  CC       wireshark-capture_sync.o
  CC       wireshark-capture_ui_utils.o
  CC       wireshark-airpcap_loader.o
  CC       wireshark-capture.o
  CC       wireshark-capture_info.o
  CC       wireshark-capture_opts.o
  CC       wireshark-color_filters.o
  CC       wireshark-file.o
  CC       wireshark-fileset.o
  CC       wireshark-filters.o
  CC       wireshark-iface_monitor.o
  CC       wireshark-proto_hier_stats.o
  CC       wireshark-summary.o
  CC       wireshark-ws80211_utils.o
  CCLD     wireshark
wireshark-iface_monitor.o: In function `iface_mon_handler2&#39;:
/home/user/Sharan/Softwares/wireshark-1.12.0/iface_monitor.c:80: undefined reference to `rtnl_link_alloc&#39;
/home/user/Sharan/Softwares/wireshark-1.12.0/iface_monitor.c:92: undefined reference to `rtnl_link_get_flags&#39;
/home/user/Sharan/Softwares/wireshark-1.12.0/iface_monitor.c:93: undefined reference to `rtnl_link_get_name&#39;
/home/user/Sharan/Softwares/wireshark-1.12.0/iface_monitor.c:110: undefined reference to `rtnl_link_put&#39;
wireshark-ws80211_utils.o: In function `get_iface_info_handler&#39;:
/home/user/Sharan/Softwares/wireshark-1.12.0/ws80211_utils.c:350: undefined reference to `genlmsg_attrlen&#39;
/home/user/Sharan/Softwares/wireshark-1.12.0/ws80211_utils.c:350: undefined reference to `genlmsg_attrdata&#39;
wireshark-ws80211_utils.o: In function `__ws80211_get_iface_info&#39;:
/home/user/Sharan/Softwares/wireshark-1.12.0/ws80211_utils.c:405: undefined reference to `genlmsg_put&#39;
wireshark-ws80211_utils.o: In function `get_phys_handler&#39;:
/home/user/Sharan/Softwares/wireshark-1.12.0/ws80211_utils.c:206: undefined reference to `genlmsg_attrlen&#39;
/home/user/Sharan/Softwares/wireshark-1.12.0/ws80211_utils.c:206: undefined reference to `genlmsg_attrdata&#39;
wireshark-ws80211_utils.o: In function `ws80211_init&#39;:
/home/user/Sharan/Softwares/wireshark-1.12.0/ws80211_utils.c:83: undefined reference to `genl_connect&#39;
/home/user/Sharan/Softwares/wireshark-1.12.0/ws80211_utils.c:89: undefined reference to `genl_ctrl_resolve&#39;
wireshark-ws80211_utils.o: In function `ws80211_create_on_demand_interface&#39;:
/home/user/Sharan/Softwares/wireshark-1.12.0/ws80211_utils.c:549: undefined reference to `genlmsg_put&#39;
wireshark-ws80211_utils.o: In function `ws80211_set_freq&#39;:
/home/user/Sharan/Softwares/wireshark-1.12.0/ws80211_utils.c:587: undefined reference to `genlmsg_put&#39;
wireshark-ws80211_utils.o: In function `ws80211_get_phys&#39;:
/home/user/Sharan/Softwares/wireshark-1.12.0/ws80211_utils.c:301: undefined reference to `genlmsg_put&#39;
collect2: error: ld returned 1 exit status
make[2]: *** [wireshark] Error 1
make[2]: Leaving directory `/home/user/Sharan/Softwares/wireshark-1.12.0&#39;
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/home/user/Sharan/Softwares/wireshark-1.12.0&#39;
make: *** [all] Error 2
[email protected]:/home/user/Sharan/Softwares/wireshark-1.12.0 #</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-make" rel="tag" title="see questions tagged &#39;make&#39;">make</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-iface_monitor.c" rel="tag" title="see questions tagged &#39;iface_monitor.c&#39;">iface_monitor.c</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '14, 03:55</strong></p><img src="https://secure.gravatar.com/avatar/46521255c9360a018c61fe9f828b7e62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sharan&#39;s gravatar image" /><p><span>Sharan</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sharan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Sep '14, 01:28</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-35927" class="comments-container"><span id="35931"></span><div id="comment-35931" class="comment"><div id="post-35931-score" class="comment-score">1</div><div class="comment-text"><p>I would guess that it's related to libnl. Try to build without it.</p></div><div id="comment-35931-info" class="comment-info"><span class="comment-age">(02 Sep '14, 08:32)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-35927" class="comment-tools"></div><div class="clear"></div><div id="comment-35927-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="35953"></span>

<div id="answer-container-35953" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35953-score" class="post-score" title="current number of votes">0</div><span id="post-35953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Goggelse says: libnl - Netlink Protocol Library Suite - Infradead.org www.infradead.org/~tgr/libnl/</p><p>It got something to do with capturing Wlan traffic, the particular code failing to build creates a toolbar to fill in channel info etc I think. For some reason configure isn't picking up the right headers I suspect or perhaps you have more than one version of libnl installed. If you don't need to do wireless captures you can do without it. if you do need it you need to install the right development package for libnl I suspect.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Sep '14, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-35953" class="comments-container"><span id="35952"></span><div id="comment-35952" class="comment"><div id="post-35952-score" class="comment-score"></div><div class="comment-text"><p>Thanks Anders. Without libnl, make is working. I got few more queries on the same line,</p><ul><li>What would be the side effects for compiling wireshark without libnl? (./configure --without-libnl).</li><li>What actually libn do?</li></ul><p>I got following warnings after compiling:</p><p><strong>(process:550): WARNING</strong> : Preference "column.hidden" has been converted to "gui.column.hidden" Save your preferences to make this change permanent.</p><p><strong>(process:550): WARNING</strong> : Preference "column.format" has been converted to "gui.column.format" Save your preferences to make this change permanent.</p></div><div id="comment-35952-info" class="comment-info"><span class="comment-age">(03 Sep '14, 03:04)</span> <span class="comment-user userinfo">Sharan</span></div></div><span id="35956"></span><div id="comment-35956" class="comment"><div id="post-35956-score" class="comment-score"></div><div class="comment-text"><p>Oh and process:550): WARNING : Preference "column.hidden" has been converted to "gui.column.hidden" Save your preferences to make this change permanent</p><p>As the Warning says the preference has been changed and the "old" and "new" preference file foramt does not match. Resaving the preferences will update to the new format.</p></div><div id="comment-35956-info" class="comment-info"><span class="comment-age">(03 Sep '14, 04:57)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="35989"></span><div id="comment-35989" class="comment"><div id="post-35989-score" class="comment-score"></div><div class="comment-text"><p>If you build without libnl, the wireless toolbar will be missing, and Wireshark won't automatically detect the addition of or removal of interfaces.</p><p>Libnl is, as the page Anders mentioned, "a collection of libraries providing APIs to netlink protocol based Linux kernel interfaces", and netlink is "a IPC mechanism primarly between the kernel and user space processes. It was designed to be a more flexible successor to ioctl to provide mainly networking related kernel configuration and monitoring interfaces."</p><p>Among other things, netlink can be used to get notifications about changes to network interfaces (so, without libnl, Wireshark can't get those notifications and can't automatically update its list of interfaces) and get information about and control wireless interfaces (so, without libnl, Wireshark can't get that information and control those interfaces, so it can't implement the wireless toolbar).</p></div><div id="comment-35989-info" class="comment-info"><span class="comment-age">(04 Sep '14, 01:37)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="35990"></span><div id="comment-35990" class="comment"><div id="post-35990-score" class="comment-score"></div><div class="comment-text"><blockquote><p>(process:550): WARNING : Preference "column.hidden" has been converted to "gui.column.hidden" Save your preferences to make this change permanent.</p></blockquote><p>That's a change between whatever version of Wireshark you were using and 1.12.0. Some GUI preferences were given new names beginning with "gui."; Wireshark converts them internally, but warns about it - if you save your preferences, they will be written out with the new name</p></div><div id="comment-35990-info" class="comment-info"><span class="comment-age">(04 Sep '14, 01:39)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-35953" class="comment-tools"></div><div class="clear"></div><div id="comment-35953-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35992"></span>

<div id="answer-container-35992" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35992-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35992-score" class="post-score" title="current number of votes">0</div><span id="post-35992-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's probably a bug somewhere in the configure script, so that it configured support in for the parts that use libnl but either didn't link with libnl or linked with the wrong version of libnl.</p><p>Could you do a <code>make distclean</code>, re-run the configure script with the same arguments that you used the last time, run <code>make V=1</code>, and file a bug on <a href="http://bugs.wireshark.org/">the Wireshark bugzilla</a>, and attach both the complete <code>config.log</code> file produced by the configure script and the output of <code>make V=1</code>?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '14, 01:52</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-35992" class="comments-container"><span id="36001"></span><div id="comment-36001" class="comment"><div id="post-36001-score" class="comment-score"></div><div class="comment-text"><p>Harris, I've raised a bug as you suggested. <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10444">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10444</a></p></div><div id="comment-36001-info" class="comment-info"><span class="comment-age">(04 Sep '14, 05:57)</span> <span class="comment-user userinfo">Sharan</span></div></div></div><div id="comment-tools-35992" class="comment-tools"></div><div class="clear"></div><div id="comment-35992-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

