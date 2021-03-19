+++
type = "question"
title = "Unable to launch Wireshark in Mavericks"
description = '''It appears that I have a continuing problem with Mavericks and Wireshark. While I had it running a bit ago, now I see that I cannot launch it from Wireshark in Applications. I see it bounce once in the Dock and then vanish. I have current versions of XQuartz and Wireshark. If I launch XQuartz and th...'''
date = "2014-04-15T02:19:00Z"
lastmod = "2014-04-23T00:59:00Z"
weight = 31834
keywords = [ "osx", "mac", "mavericks" ]
aliases = [ "/questions/31834" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to launch Wireshark in Mavericks](/questions/31834/unable-to-launch-wireshark-in-mavericks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31834-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>It appears that I have a continuing problem with Mavericks and Wireshark. While I had it running a bit ago, now I see that I cannot launch it from Wireshark in Applications. I see it bounce once in the Dock and then vanish. I have current versions of XQuartz and Wireshark. If I launch XQuartz and then 'wireshark' from an xterm/Terminal window in that X11 environment, Wireshark will appear after several minutes and I can work. (The long pause at first-run has to do with building a font cache. Once done, subsequent launches go quicker.)</p><p>I uninstalled Wireshark using AppDelete and then reinstalled with no change in this one-bounce-and-gone behaviour.</p><p>If quit Wireshark and XQuartz and then try from a regular Terminal window, I get:</p><pre><code>===

$ wireshark

2014-04-15 19:09:59.966 defaults[37571:507]

The domain/default pair of (kCFPreferencesAnyApplication, AppleAquaColorVariant) does not exist

(process:37561): Gtk-WARNING **: Locale not supported by C library.

Using the fallback &#39;C&#39; locale.

(wireshark-bin:37561): Gtk-WARNING **: cannot open display:

===</code></pre><p>Looks like environment variables are corrupted or missing and the X11 display is not called. What might be handy to know is how to return to a clean slate before installing XQuartz and Wireshark. I am guessing some things that hang around after an uninstall/reinstall are causing trouble.</p><p>Any ideas? I figure if I can launch it from Terminal, it will launch from Applications.</p></div><div id="question-tags" class="tags-container tags">osx mac mavericks</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '14, 02:19</strong></p><img src="https://secure.gravatar.com/avatar/15b9a6ab9c13f571913a7e30512d0099?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pjconmac&#39;s gravatar image" /><p>pjconmac<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pjconmac has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 17 Apr '14, 03:10</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-31834" class="comments-container"></div><div id="comment-tools-31834" class="comment-tools"></div><div class="clear"></div><div id="comment-31834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="31954"></span>

<div id="answer-container-31954" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31954-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have seen threads on this unusual behavior before. Most will discuss cleaning up XQuartz. When I encountered an issue that seemed very similar to yours, I reinstall XQuartz and it resolved my issue.</p><p>Here is another very active thread about unusual issues under Mavericks:</p><p><a href="http://ask.wireshark.org/questions/26326/apple-maverick-and-x11">http://ask.wireshark.org/questions/26326/apple-maverick-and-x11</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '14, 15:31</strong></p><img src="https://secure.gravatar.com/avatar/73bcc9038f127739c0856748313dbe73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stjaru&#39;s gravatar image" /><p>stjaru<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stjaru has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Apr '14, 15:32</p></div></div><div id="comments-container-31954" class="comments-container"></div><div id="comment-tools-31954" class="comment-tools"></div><div class="clear"></div><div id="comment-31954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32029"></span>

<div id="answer-container-32029" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32029-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>With OS X Mountain Lion and newer, Apple no longer ships the X11 framework with the Core OS. You'll have to download and install XQuartz:</p><p><a href="http://support.apple.com/kb/ht5293">http://support.apple.com/kb/ht5293</a></p><p><a href="https://xquartz.macosforge.org/landing/">https://xquartz.macosforge.org/landing/</a></p><p>I've also noticed that some major updates (10.9.0 -&gt; 10.9.1) have forced me to re-install XQuartz.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '14, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/5b11899f6ef8d3994b8bcc4e5c27609f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mire3212&#39;s gravatar image" /><p>mire3212<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mire3212 has no accepted answers">0%</span></p></div></div><div id="comments-container-32029" class="comments-container"></div><div id="comment-tools-32029" class="comment-tools"></div><div class="clear"></div><div id="comment-32029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32089"></span>

<div id="answer-container-32089" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32089-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I fully uninstalled Wireshark, reinstalled and tested, seeing the same behaviour. I reinstalled XQuartz as suggested above, seeing the same behaviour when launching Wireshark. By the way, there are details on uninstalling Wireshark in the README that accompanies the Wireshark installer. There are also several symlink files (like 'tshark') that point to the 'wireshark' item, all in '/usr/local/bin'. I deleted all those during that session also. (I did notice that 'ls -l' showed the owner of 'wireshark' as 'macports'. I have MacPorts installed but not its wireshark package.)</p><p>My current solution is to install the latest development version of Wireshark, which is based on Qt and does not require X11/XQuartz, It is a full OS X application. It has quite a different look but should work just fine. If not, I can return to the X11/xterm-launched 'wireshark' method.</p><p>Cheers,</p><p>Paul</p><p>P.S. I have a post on the other Mavericks discussion page noted above but in another account name. I gave up frustrating myself with its OpenID sign-in nonsense and created a direct account here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '14, 00:59</strong></p><img src="https://secure.gravatar.com/avatar/15b9a6ab9c13f571913a7e30512d0099?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pjconmac&#39;s gravatar image" /><p>pjconmac<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pjconmac has no accepted answers">0%</span></p></div></div><div id="comments-container-32089" class="comments-container"><span id="32636"></span><div id="comment-32636" class="comment"><div id="post-32636-score" class="comment-score"></div><div class="comment-text"><p>The issue is that the libs in wireshark reference X11 libs in /usr/X11/* - in Mavericks this is just a bunch of stubs which will abort your application and tell you to install XQuartz (which you already have). To get around it, one would have to rebuild the whole stack to link against the libs in /opt/X11 instead. I used the following trick to get around it: <a href="http://superuser.com/a/650933">http://superuser.com/a/650933</a></p><p>(The Qt version still requires a bit of tweaking before I'd be ready to switch.)</p></div><div id="comment-32636-info" class="comment-info"><span class="comment-age">(08 May '14, 03:32)</span> mstorsjo</div></div><span id="32649"></span><div id="comment-32649" class="comment"><div id="post-32649-score" class="comment-score"></div><div class="comment-text"><p>Installing XQuartz doesn't point those stubs at <code>/opt</code>? That's really annoying - if you're going to have stubs for not-present software that says "hey, would you like to install XXX?", installing XXX should replace the stubs. Apple's command-line tools do that, and so do at least some command-line tools on Debian and relatives.</p><p>For what it's worth, on my Mavericks VM, with XQuartz installed, <code>/usr/X11</code> is a symlink to <code>/opt/X11</code>.</p><p>(Also, for what it's worth, on my Mountain Lion main machine, Safari thinks "XQuartz" and "Xquartz" are both misspellings. :-))</p></div><div id="comment-32649-info" class="comment-info"><span class="comment-age">(08 May '14, 16:52)</span> Guy Harris ♦♦</div></div><span id="32650"></span><div id="comment-32650" class="comment"><div id="post-32650-score" class="comment-score"></div><div class="comment-text"><p>At the moment, as I mentioned I have the Qt version of Wireshark installed. After reading these two comments I opened a Terminal session. I 'cd' into '/usr/X11' did a listing, 'cd' into subdirectory 'lib' and did a listing and copied the screen output to a text editor window (in BBEdit.) I cleared the screen and did the same for '/opt/X11' and its 'lib' subdirectory.</p><p>date; cd /opt/X11/; ls -l; cd lib; ls -l</p><p>date; cd /usr/X11/; ls -l; cd lib; ls -l</p><p>Then, I did a compare on the two file lists. They are the same. Is this because of the Qt-version? Am I missing something? I can do an uninstall of XQuartz and Wireshark and do this routine again. Thoughts?</p></div><div id="comment-32650-info" class="comment-info"><span class="comment-age">(08 May '14, 17:10)</span> pjconmac</div></div><span id="32651"></span><div id="comment-32651" class="comment"><div id="post-32651-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Then, I did a compare on the two file lists. They are the same</p></blockquote><p>Try <code>ls -ld /usr/X11</code>. If it reports something such as</p><pre><code>lrwxr-xr-x  1 root  wheel  8 Sep  7  2012 /usr/X11 -&gt; /opt/X11</code></pre><p>then the file lists are the same because the <em>directories</em> are the same - <code>/usr/X11</code>, in that case, is just a symlink to <code>/opt/X11</code>.</p><blockquote><p>Is this because of the Qt-version?</p></blockquote><p>No. The Qt version does not use X11 on OS X.</p></div><div id="comment-32651-info" class="comment-info"><span class="comment-age">(08 May '14, 17:19)</span> Guy Harris ♦♦</div></div><span id="32652"></span><div id="comment-32652" class="comment"><div id="post-32652-score" class="comment-score"></div><div class="comment-text"><p>Ah, so it is... I missed that detail:</p><p>lrwxr-xr-x 1 root wheel 8 14 Nov 12:27 /usr/[email protected] -&gt; /opt/X11</p></div><div id="comment-32652-info" class="comment-info"><span class="comment-age">(08 May '14, 17:23)</span> pjconmac</div></div><span id="32714"></span><div id="comment-32714" class="comment not_top_scorer"><div id="post-32714-score" class="comment-score"></div><div class="comment-text"><p>To follow up - I reinstalled XQuartz 2.7.5 and then I got the /usr/X11 symlink set up as others had it. (In my case, I had installed XQuartz 2.7.5 before upgrading to Mavericks, and previously didn't realize that reinstalling it would help.)</p></div><div id="comment-32714-info" class="comment-info"><span class="comment-age">(11 May '14, 13:01)</span> mstorsjo</div></div></div><div id="comment-tools-32089" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-32089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

