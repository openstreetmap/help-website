+++
type = "question"
title = "Impossible to make wireshark 2.2.2 rpm package on centos 6.5 ?"
description = '''I am using centos 6.5, and trying to build a wireshark 2.2.2 rpm from the source code. this is what I get after running ./configure The Wireshark package has been configured with the following options:  GLib version : v2.28.8  Build wireshark : no  Build wireshark-gtk : yes (with GTK+ v2.24.23)  Bui...'''
date = "2016-11-30T22:54:00Z"
lastmod = "2016-12-01T23:13:00Z"
weight = 57744
keywords = [ "rpm-package", "rpm", "centos", "wireshark" ]
aliases = [ "/questions/57744" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Impossible to make wireshark 2.2.2 rpm package on centos 6.5 ?](/questions/57744/impossible-to-make-wireshark-222-rpm-package-on-centos-65)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57744-score" class="post-score" title="current number of votes">0</div><span id="post-57744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using centos 6.5, and trying to build a wireshark 2.2.2 rpm from the source code.</p><p>this is what I get after running ./configure</p><pre><code>The Wireshark package has been configured with the following options:
                   GLib version : v2.28.8
                Build wireshark : no
            Build wireshark-gtk : yes (with GTK+ v2.24.23)
                   Build tshark : yes
                  Build tfshark : no
                 Build capinfos : yes
                  Build captype : yes
                  Build editcap : yes
                  Build dumpcap : yes
                 Build mergecap : yes
               Build reordercap : yes
                Build text2pcap : yes
                  Build randpkt : yes
                   Build dftest : yes
                 Build rawshark : yes
              Build androiddump : yes
                  Build sshdump : no
                Build ciscodump : no
              Build randpktdump : yes
                    Build echld : no

   Save files as pcap-ng by default : yes
Install dumpcap with capabilities : no
         Install dumpcap setuid : no
              Use dumpcap group : (none)
                    Use plugins : yes
   Use external capture sources : yes
                Use Lua library : no
            Build Qt RTP player : no
          Build GTK+ RTP player : no
         Build profile binaries : no
               Use pcap library : yes
               Use zlib library : yes
           Use kerberos library : yes (MIT)
             Use c-ares library : no (name resolution will be disabled)
            Use SMI MIB library : no
         Use GNU gcrypt library : yes
         Use SSL crypto library : no
             Use GnuTLS library : no
 Use POSIX capabilities library : no
              Use GeoIP library : no
             Use libssh library : no
        Have ssh_userauth_agent : no
                 Use nl library : no
          Use SBC codec library : no</code></pre><p>I have updated ran this command too to resolve any dependency issues which might be there..</p><pre><code>yum install -y gcc-c++ bison flex gtk2 gtk2-devel libpcap-devel</code></pre><p>But this is the error I keep getting when i run <strong>make rpm-package</strong></p><pre><code>make[2]: Entering directory `/tmp/wireshark-2.2.2/ui/gtk&#39;
make[2]: Leaving directory `/tmp/wireshark-2.2.2/ui/gtk&#39;
 (cd ui/qt &amp;&amp; make  top_distdir=../../wireshark-2.2.2     distdir=../../wireshark-2.2.2/ui/qt \
     am__remove_distdir=: am__skip_length_check=: am__skip_mode_fix=: distdir)
make[2]: Entering directory `/tmp/wireshark-2.2.2/ui/qt&#39;
  LRELEASE   wireshark_de.qm
/bin/sh: -silent: command not found
make[2]: *** [wireshark_de.qm] Error 127
make[2]: Leaving directory `/tmp/wireshark-2.2.2/ui/qt&#39;
make[1]: *** [distdir] Error 1
make[1]: Leaving directory `/tmp/wireshark-2.2.2&#39;
make: *** [dist] Error 2</code></pre><p>dont know what to do about it, has anyone else had successfully made <strong>wireshark 2.2.2 rpm</strong> for centos 6.x</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rpm-package" rel="tag" title="see questions tagged &#39;rpm-package&#39;">rpm-package</span> <span class="post-tag tag-link-rpm" rel="tag" title="see questions tagged &#39;rpm&#39;">rpm</span> <span class="post-tag tag-link-centos" rel="tag" title="see questions tagged &#39;centos&#39;">centos</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Nov '16, 22:54</strong></p><img src="https://secure.gravatar.com/avatar/1fce6962babfed133dfb8b1cc2a5d38c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="himanshu097&#39;s gravatar image" /><p><span>himanshu097</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="himanshu097 has no accepted answers">0%</span></p></div></div><div id="comments-container-57744" class="comments-container"></div><div id="comment-tools-57744" class="comment-tools"></div><div class="clear"></div><div id="comment-57744-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="57766"></span>

<div id="answer-container-57766" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57766-score" class="post-score" title="current number of votes">1</div><span id="post-57766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="himanshu097 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Actually the RPMs now follow what you chose in ./configure (at for some options). It <em>should</em> work to build just the Gtk version (useful for RHEL 6 since--IIRC--the Qt version won't build there).</p><p>The problem here is that it was trying to build the Qt I18N stuff without having detected Qt. I <a href="https://code.wireshark.org/review/#/c/19004/">just backported João's fix</a> to the 2.2 branch so this will work in the next version. (In the meantime you could manually apply the patch.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '16, 10:53</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-57766" class="comments-container"></div><div id="comment-tools-57766" class="comment-tools"></div><div class="clear"></div><div id="comment-57766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57748"></span>

<div id="answer-container-57748" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57748-score" class="post-score" title="current number of votes">0</div><span id="post-57748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Th RPM package assumes that you will also build the Qt based GUI. And it looks like you have not installed the corresponding dependencies (as seen in the configure output): Build wireshark : no</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '16, 01:44</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-57748" class="comments-container"><span id="57777"></span><div id="comment-57777" class="comment"><div id="post-57777-score" class="comment-score"></div><div class="comment-text"><p>I had configured it explicitly to not use QT, still it didnot impact how dist was made.</p></div><div id="comment-57777-info" class="comment-info"><span class="comment-age">(01 Dec '16, 23:13)</span> <span class="comment-user userinfo">himanshu097</span></div></div></div><div id="comment-tools-57748" class="comment-tools"></div><div class="clear"></div><div id="comment-57748-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

