+++
type = "question"
title = "[closed] glib installation failing with parse error"
description = '''Hi,  We want to install the wireshark development kit, and we have successfully installed autoconf, automake and libtool. But when we tried to install the wireshark, it gave the dependency error on gpk, and gpk had a dependency on glib. We are getting the following error when we try to install glib....'''
date = "2013-09-18T20:45:00Z"
lastmod = "2013-09-19T07:13:00Z"
weight = 24937
keywords = [ "python", "glib", "gpk" ]
aliases = [ "/questions/24937" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] glib installation failing with parse error](/questions/24937/glib-installation-failing-with-parse-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24937-score" class="post-score" title="current number of votes">0</div><span id="post-24937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We want to install the wireshark development kit, and we have successfully installed autoconf, automake and libtool. But when we tried to install the wireshark, it gave the dependency error on gpk, and gpk had a dependency on glib. We are getting the following error when we try to install glib. Python 2.75 is installed. Please let us know.</p><pre><code>[[email protected] glib-2.36.4]# python --version
Python 2.7.5

/usr/bin/msgfmt -o test.mo ./de.po; \
        /bin/mkdir -p de/LC_MESSAGES; \
        cp -f test.mo de/LC_MESSAGES
./de.po:15: keyword &quot;msgctxt&quot; unknown
./de.po:15:8: parse error
/usr/bin/msgfmt: found 2 fatal errors
cp: cannot stat `test.mo&#39;: No such file or directory
make[5]: *** [test.mo] Error 1
make[5]: Leaving directory `/root/gpalanka/glib-2.36.4/gio/tests&#39;
make[4]: *** [install-recursive] Error 1
make[4]: Leaving directory `/root/gpalanka/glib-2.36.4/gio/tests&#39;
make[3]: *** [install] Error 2
make[3]: Leaving directory `/root/gpalanka/glib-2.36.4/gio/tests&#39;
make[2]: *** [install-recursive] Error 1
make[2]: Leaving directory `/root/gpalanka/glib-2.36.4/gio&#39;
make[1]: *** [install] Error 2
make[1]: Leaving directory `/root/gpalanka/glib-2.36.4/gio&#39;
make: *** [install-recursive] Error 1
[[email protected] glib-2.36.4]# pwd
/root/gpalanka/glib-2.36.4
[[email protected] glib-2.36.4]#

[[email protected] gpalanka]# autoconf --version
autoconf (GNU Autoconf) 2.64
Copyright (C) 2009 Free Software Foundation, Inc.
License GPLv2+: GNU GPL version 2 or later
&lt;http://gnu.org/licenses/old-licenses/gpl-2.0.html&gt;
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by David J. MacKenzie and Akim Demaille.
[[email protected] gpalanka]# automake --version
automake (GNU automake) 1.11
Copyright (C) 2009 Free Software Foundation, Inc.
License GPLv2+: GNU GPL version 2 or later &lt;http://gnu.org/licenses/gpl-2.0.html&gt;
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Tom Tromey &lt;[email protected]&gt;
       and Alexandre Duret-Lutz &lt;[email protected]&gt;.
[[email protected] gpalanka]# libtool --version
ltmain.sh (GNU libtool) 2.2.6
Written by Gordon Matzigkeit &lt;[email protected]&gt;, 1996

Copyright (C) 2008 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
[[email protected] gpalanka]#</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-glib" rel="tag" title="see questions tagged &#39;glib&#39;">glib</span> <span class="post-tag tag-link-gpk" rel="tag" title="see questions tagged &#39;gpk&#39;">gpk</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '13, 20:45</strong></p><img src="https://secure.gravatar.com/avatar/7a7b8901328249aa8d526a374e2540b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sahana&#39;s gravatar image" /><p><span>Sahana</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sahana has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> closed <strong>19 Sep '13, 07:12</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-24937" class="comments-container"><span id="24958"></span><div id="comment-24958" class="comment"><div id="post-24958-score" class="comment-score"></div><div class="comment-text"><p>This isn't the place to ask for help installing glib--there are many other places for that type of question.</p></div><div id="comment-24958-info" class="comment-info"><span class="comment-age">(19 Sep '13, 07:13)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-24937" class="comment-tools"></div><div class="clear"></div><div id="comment-24937-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by JeffMorriss 19 Sep '13, 07:12

</div>

</div>

</div>

