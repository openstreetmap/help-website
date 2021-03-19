+++
type = "question"
title = "Wireshark source build errors during msbuild"
description = '''After 51 minute of building source, I get 2 warnings and 4 errors. It looks as though its looking for the &quot;guide docs&quot; that don&#x27;t exist? I&#x27;m using the Wireshark source files &quot;as is&quot; and have made no modifications to the build scripts, etc. I did a clean, prepared the sources with no issues, then ran...'''
date = "2016-09-27T05:46:00Z"
lastmod = "2016-09-28T08:06:00Z"
weight = 55899
keywords = [ "64bit", "msbuild", "win7" ]
aliases = [ "/questions/55899" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark source build errors during msbuild](/questions/55899/wireshark-source-build-errors-during-msbuild)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55899-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After 51 minute of building source, I get 2 warnings and 4 errors. It looks as though its looking for the "guide docs" that don't exist? I'm using the Wireshark source files "as is" and have made no modifications to the build scripts, etc. I did a clean, prepared the sources with no issues, then ran the build. Any help would be greatly appreciated :)</p><p>Build FAILED.</p><pre><code>   &quot;C:\wireshark-2.2.0\buildx64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;C:\wireshark-2.2.0\buildx64\docbook\generate_user-guide.xml.vcxproj.metaproj&quot; (default target) (31) -&gt;
   &quot;C:\wireshark-2.2.0\buildx64\docbook\generate_user-guide.xml.vcxproj&quot; (default target) (101) -&gt;
   (CustomBuild target) -&gt;
     asciidoc : warning : user-guide.asciidoc: line 3: {include:/cygdrive/c/wireshark-2.2.0/docbook/user-guide-docinfo.xml}: file does not exist [C:\wireshark-2.2.0\buildx64\docbook\generate_user-guide.xml.vcxproj]

   &quot;C:\wireshark-2.2.0\buildx64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;C:\wireshark-2.2.0\buildx64\docbook\generate_developer-guide.xml.vcxproj.metaproj&quot; (default target) (30) -&gt;
   &quot;C:\wireshark-2.2.0\buildx64\docbook\generate_developer-guide.xml.vcxproj&quot; (default target) (100) -&gt;
     asciidoc : warning : developer-guide.asciidoc: line 3: {include:/cygdrive/c/wireshark-2.2.0/docbook/developer-guide-docinfo.xml}: file does not exist [C:\wireshark-2.2.0\buildx64\docbook\generate_developer-guide.xml.vcxproj]

   &quot;C:\wireshark-2.2.0\buildx64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;C:\wireshark-2.2.0\buildx64\ui\ui.vcxproj.metaproj&quot; (default target) (61) -&gt;
   &quot;C:\wireshark-2.2.0\buildx64\ui\ui.vcxproj&quot; (default target) (108) -&gt;
   (CustomBuild target) -&gt;
     C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. [C:\wireshark-2.2.0\buildx64\ui\ui.vcxproj]

   &quot;C:\wireshark-2.2.0\buildx64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;C:\wireshark-2.2.0\buildx64\epan\dfilter\dfilter.vcxproj.metaproj&quot; (default target) (18) -&gt;
   &quot;C:\wireshark-2.2.0\buildx64\epan\dfilter\dfilter.vcxproj&quot; (default target) (110) -&gt;
     C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. [C:\wireshark-2.2.0\buildx64\epan\dfilter\dfilter.vcxproj]

   &quot;C:\wireshark-2.2.0\buildx64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;C:\wireshark-2.2.0\buildx64\text2pcap.vcxproj.metaproj&quot; (default target) (56) -&gt;
   &quot;C:\wireshark-2.2.0\buildx64\text2pcap.vcxproj&quot; (default target) (124) -&gt;
     C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. [C:\wireshark-2.2.0\buildx64\text2pcap.vcxproj]

   &quot;C:\wireshark-2.2.0\buildx64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;C:\wireshark-2.2.0\buildx64\wiretap\wiretap.vcxproj.metaproj&quot; (default target) (72) -&gt;
   &quot;C:\wireshark-2.2.0\buildx64\wiretap\wiretap.vcxproj&quot; (default target) (125) -&gt;
     C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. [C:\wireshark-2.2.0\buildx64\wiretap\wiretap.vcxproj]

2 Warning(s)
4 Error(s)</code></pre><p>Time Elapsed 00:51:07.21</p></div><div id="question-tags" class="tags-container tags">64bit msbuild win7</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '16, 05:46</strong></p><img src="https://secure.gravatar.com/avatar/b363fb1dfec547bd68fa5e3eae8836a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike_P&#39;s gravatar image" /><p>Mike_P<br />
<span class="score" title="30 reputation points">30</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike_P has no accepted answers">0%</span></p></div></div><div id="comments-container-55899" class="comments-container"><span id="55900"></span><div id="comment-55900" class="comment"><div id="post-55900-score" class="comment-score"></div><div class="comment-text"><p>So after doing searching, I can see that I'm not the only one that had this issue. <a href="https://ask.wireshark.org/questions/55094/build-wireshark-failed">https://ask.wireshark.org/questions/55094/build-wireshark-failed</a></p><p>In that case, they were not connected to the internet and could not make the download call to pull htmlhelp.xsl from the download site during the build. Or at least that's what is thought.</p><p>I am connected to the internet and can manually download the file. I've placed it in my wireshark\docbook directory in the source, edited the custom_layer_chm.xsl to point to the local copy and will attempt a new build to see if it works.</p></div><div id="comment-55900-info" class="comment-info"><span class="comment-age">(27 Sep '16, 05:58)</span> Mike_P</div></div><span id="55903"></span><div id="comment-55903" class="comment"><div id="post-55903-score" class="comment-score"></div><div class="comment-text"><p>The other question you refer to showed an explicit error in trying to retrieve the file, but that isn't what you're seeing.</p><p>Your build is complaining about the input to asciidoc, the .xml versions of the .asciidoc sources, that are built by running the a2x executable.</p><p>It looks like your build environment possibly isn't complete, have you installed all the required Cygwin packages?</p></div><div id="comment-55903-info" class="comment-info"><span class="comment-age">(27 Sep '16, 06:37)</span> grahamb ♦</div></div><span id="55905"></span><div id="comment-55905" class="comment"><div id="post-55905-score" class="comment-score"></div><div class="comment-text"><p>Checking my cygwin install now.</p></div><div id="comment-55905-info" class="comment-info"><span class="comment-age">(27 Sep '16, 06:42)</span> Mike_P</div></div><span id="55906"></span><div id="comment-55906" class="comment"><div id="post-55906-score" class="comment-score"></div><div class="comment-text"><p>Have you managed to build Wireshark on this machine before? Are you building from a Git clone or a source tarball or some other means?</p></div><div id="comment-55906-info" class="comment-info"><span class="comment-age">(27 Sep '16, 06:47)</span> grahamb ♦</div></div><span id="55907"></span><div id="comment-55907" class="comment"><div id="post-55907-score" class="comment-score"></div><div class="comment-text"><p>First build with source tarball on new pc with new wireshark setup using the online guide <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html.">https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html.</a> I've been building for a few years on another Windows machine using cmake.</p></div><div id="comment-55907-info" class="comment-info"><span class="comment-age">(27 Sep '16, 06:52)</span> Mike_P</div></div><span id="55909"></span><div id="comment-55909" class="comment not_top_scorer"><div id="post-55909-score" class="comment-score"></div><div class="comment-text"><p>Building on Windows from a source tarball isn't checked by the automatic build systems and isn't done by most devs either, so doing it that way might have issues that have gone unnoticed.</p><p>Building from a git clone is checked and is what most devs do, so is likely to be more successful.</p><p>However I don't "think" the sources of your source files are the problem here.</p></div><div id="comment-55909-info" class="comment-info"><span class="comment-age">(27 Sep '16, 07:00)</span> grahamb ♦</div></div><span id="55914"></span><div id="comment-55914" class="comment not_top_scorer"><div id="post-55914-score" class="comment-score"></div><div class="comment-text"><p>Checked cygwin. Install was per the recommendations. Rebooted just in case. Cleaned my build directory, prepped source, then msbuild. Same errors.</p></div><div id="comment-55914-info" class="comment-info"><span class="comment-age">(27 Sep '16, 07:58)</span> Mike_P</div></div><span id="55915"></span><div id="comment-55915" class="comment not_top_scorer"><div id="post-55915-score" class="comment-score"></div><div class="comment-text"><p>My path:</p><pre><code>C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\IDE\CommonExtensions\Microsoft\TestWindow
C:\Program Files (x86)\MSBuild\12.0\bin\amd64
C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\BIN\amd64
C:\windows\Microsoft.NET\Framework64\v4.0.30319
C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\VCPackages
C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\IDE
C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\Tools
C:\Program Files (x86)\HTML Help Workshop
C:\Program Files (x86)\Microsoft Visual Studio 12.0\Team Tools\Performance Tools\x64
C:\Program Files (x86)\Microsoft Visual Studio 12.0\Team Tools\Performance Tools
C:\Program Files (x86)\Windows Kits\8.1\bin\x64
C:\Program Files (x86)\Windows Kits\8.1\bin\x86
C:\Program Files (x86)\Microsoft SDKs\Windows\v8.1A\bin\NETFX 4.5.1 Tools\x64\
C:\Program Files\CMake\bin
c:\ccrypt
C:\Python35\Scripts\
C:\Python35\
C:\Qt\Qt5.7.0\5.7\msvc2013_64
C:\cygwin64
C:\Program Files (x86)\Common Files\NetSarang
C:\ProgramData\Oracle\Java\javapath
C:\windows\system32
C:\windows
C:\windows\System32\Wbem
C:\Program Files\ActivIdentity\ActivClient\
C:\Program Files (x86)\ActivIdentity\ActivClient\
C:\Program Files\Tumbleweed\Desktop Validator\
C:\Program Files\Tumbleweed\Desktop Validator\x86
C:\windows\System32\WindowsPowerShell\v1.0\
C:\windows\System32\WindowsPowerShell\v1.0\
C:\ProgramData\chocolatey\bin
C:\Program Files\Microsoft SQL Server\130\Tools\Binn\
C:\Program Files (x86)\GnuWin32\bin
C:\Program Files (x86)\Windows Kits\8.1\Windows Performance Toolkit\
C:\Program Files\Microsoft SQL Server\110\Tools\Binn\
C:\Program Files (x86)\Microsoft SDKs\TypeScript\1.0\
C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC</code></pre><p>system values:</p><pre><code>WIRESHARK_BASE_DIR=C:\wireshark-2.2.0
WIRESHARK_CYGWIN_INSTALL_PATH=C:\cygwin64
WIRESHARK_TARGET_PLATFORM=win64</code></pre></div><div id="comment-55915-info" class="comment-info"><span class="comment-age">(27 Sep '16, 08:13)</span> Mike_P</div></div><span id="55916"></span><div id="comment-55916" class="comment not_top_scorer"><div id="post-55916-score" class="comment-score"></div><div class="comment-text"><p>Nothing too drastic there.</p><p>I think the issue is either CMake detection of the build tools, or something wrong with a2x in Cygwin.</p><p>What's the output of <code>C:\Cygwin64\bin\cygcheck -c</code>? Redirecting it to a text file makes it go much quicker.</p></div><div id="comment-55916-info" class="comment-info"><span class="comment-age">(27 Sep '16, 08:43)</span> grahamb ♦</div></div><span id="55917"></span><div id="comment-55917" class="comment not_top_scorer"><div id="post-55917-score" class="comment-score"></div><div class="comment-text"><p>All was OK. I'd post the list, but its too big for the comments section.</p><p>a2x in cygwin? Should I see that in the cygcheck list? I do not.</p></div><div id="comment-55917-info" class="comment-info"><span class="comment-age">(27 Sep '16, 08:49)</span> Mike_P</div></div><span id="55918"></span><div id="comment-55918" class="comment not_top_scorer"><div id="post-55918-score" class="comment-score"></div><div class="comment-text"><p>When a post is too big for a comment, post it as an answer, then convert it to a comment under either the question or an answer as appropriate using the buttons under the answer. For bonus points add the "code" formatting to the list so it displays nicely.</p><p>a2x is a symlink to a2x.py, both in the Cygwin bin directory, it doesn't show up in the cygcheck package output as it's part of the asciidoc package.</p></div><div id="comment-55918-info" class="comment-info"><span class="comment-age">(27 Sep '16, 08:54)</span> grahamb ♦</div></div><span id="55921"></span><div id="comment-55921" class="comment not_top_scorer"><div id="post-55921-score" class="comment-score"></div><div class="comment-text"><p><code>Cygwin Package Information Package                             Version                      Status _autorebase                         001004-1                     OK alternatives                        1.3.30c-10                   OK asciidoc                            8.6.8-1                      OK base-cygwin                         3.8-1                        OK base-files                          4.2-4                        OK bash                                4.3.46-7                     OK bc                                  1.06.95-2                    OK biber                               2.5-1                        OK binutils                            2.25-4                       OK bison                               3.0.4-1                      OK build-docbook-catalog               1.5-2                        OK bzip2                               1.0.6-2                      OK ca-certificates                     2.9-1                        OK ccrypt                              1.10-1                       OK clisp                               2.49-6.20150312hg15611       OK coreutils                           8.25-3                       OK csih                                0.9.9-1                      OK cygrunsrv                           1.62-1                       OK cygutils                            1.4.15-2                     OK cygwin                              2.6.0-1                      OK cygwin-devel                        2.6.0-1                      OK dash                                0.5.8-3                      OK dblatex                             0.3.7-1                      OK dejavu-fonts                        2.37-1                       OK desktop-file-utils                  0.23-1                       OK dialog                              1.3-2.20160828               OK diffutils                           3.5-1                        OK docbook-xml45                       4.5-1                        OK docbook-xsl                         1.77.1-1                     OK dri-drivers                         12.0.2-1                     OK ed                                  1.13-1                       OK editrights                          1.03-1                       OK file                                5.25-1                       OK findutils                           4.6.0-1                      OK flex                                2.6.1-1                      OK gamin                               0.1.10-15                    OK gawk                                4.1.4-1                      OK getent                              2.18.90-4                    OK ghostscript                         9.19-1                       OK ghostscript-fonts-other             6.0-1                        OK ghostscript-fonts-std               8.11-1                       OK git                                 2.8.3-1                      OK gnupg                               1.4.21-1                     OK grep                                2.25-1                       OK groff                               1.22.3-1                     OK gsettings-desktop-schemas           3.18.1-1                     OK gzip                                1.8-1                        OK hostname                            3.13-1                       OK ImageMagick                         6.9.5.7-1                    OK info                                6.3-1                        OK ipc-utils                           1.0-2                        OK less                                481-1                        OK libargp                             20110921-3                   OK libattr1                            2.4.46-1                     OK libautotrace3                       0.31.1-17                    OK libblkid1                           2.25.2-2                     OK libbz2_1                            1.0.6-2                      OK libcairo2                           1.14.4-1                     OK libcom_err2                         1.42.12-2                    OK libcroco0.6_3                       0.6.11-1                     OK libcrypt0                           1.4-1                        OK libcurl4                            7.50.3-1                     OK libdatrie1                          0.2.8-1                      OK libdb5.3                            5.3.28-1                     OK libdialog13                         1.3-2.20160828               OK libedit0                            20130712-1                   OK libEGL1                             12.0.2-1                     OK libEMF1                             1.0.8-1                      OK libexpat1                           2.2.0-0                      OK libfam0                             0.1.10-15                    OK libffi6                             3.2.1-2                      OK libfftw3_3                          3.3.5-1                      OK libfontconfig-common                2.12.1-1                     OK libfontconfig1                      2.12.1-1                     OK libfpx1                             1.3.1.4-1                    OK libfreetype6                        2.6.5-1                      OK libgc1                              7.2d-2                       OK libgcc1                             5.4.0-1                      OK libgcrypt20                         1.6.6-1                      OK libgd3                              2.2.3-1                      OK libgdbm4                            1.11-1                       OK libgdk_pixbuf2.0_0                  2.32.3-1                     OK libgfortran3                        5.4.0-1                      OK libgif4                             4.1.6-12                     OK libGL1                              12.0.2-1                     OK libglapi0                           12.0.2-1                     OK libglib2.0_0                        2.46.2-4                     OK libgmp10                            6.1.1-1                      OK libgnutls28                         3.3.17-1                     OK libgomp1                            5.4.0-1                      OK libgpg-error0                       1.24-1                       OK libgraphite2_3                      1.3.6-1                      OK libgs9                              9.19-1                       OK libgssapi_krb5_2                    1.14.4-1                     OK libharfbuzz-icu0                    1.2.7-1                      OK libharfbuzz0                        1.2.7-1                      OK libhogweed2                         2.7.1-1                      OK libICE6                             1.0.9-1                      OK libiconv                            1.14-3                       OK libiconv2                           1.14-3                       OK libicu57                            57.1-1                       OK libidn11                            1.29-1                       OK libintl8                            0.19.7-1                     OK libjasper1                          1.900.1-15                   OK libjbig2                            2.0-14                       OK libjpeg8                            1.5.0-1                      OK libk5crypto3                        1.14.4-1                     OK libkpathsea6                        20160520-3                   OK libkrb5_3                           1.14.4-1                     OK libkrb5support0                     1.14.4-1                     OK liblapack0                          3.6.1-1                      OK liblcms2_2                          2.6-1                        OK libllvm3.8                          3.8.1-1                      OK liblzma5                            5.2.2-1                      OK liblzo2_2                           2.08-1                       OK libMagickC++6_6                     6.9.5.7-1                    OK libMagickCore6_2                    6.9.5.7-1                    OK libMagickWand6_2                    6.9.5.7-1                    OK libming1                            0.4.7-2                      OK libmpfr4                            3.1.4-1                      OK libncursesw10                       6.0-8.20160917               OK libnetpbm10                         10.74.05-1                   OK libnettle4                          2.7.1-1                      OK libnghttp2_14                       1.14.0-1                     OK libnspr4                            4.10.10-1                    OK libnss3                             3.20.1-1                     OK libopenjp2_7                        2.1.1-1                      OK libopenjpeg1                        1.5.2-3                      OK libopenldap2_4_2                    2.4.42-1                     OK libopenssl100                       1.0.2j-1                     OK libp11-kit0                         0.22.1-1                     OK libpango1.0_0                       1.38.1-1                     OK libpaper-common                     1.1.24-2                     OK libpaper1                           1.1.24-2                     OK libpcre1                            8.39-1                       OK libpipeline1                        1.4.0-1                      OK libpixman1_0                        0.34.0-1                     OK libplotter2                         2.6-5                        OK libpng16                            1.6.24-1                     OK libpoppler62                        0.45.0-1                     OK libpopt-common                      1.16-2                       OK libpopt0                            1.16-2                       OK libpsl5                             0.14.0-1                     OK libpstoedit0                        3.70-2                       OK libptexenc1                         20160520-3                   OK libquadmath0                        5.4.0-1                      OK libreadline7                        6.3.8-1                      OK librsvg2_2                          2.40.11-1                    OK libsasl2_3                          2.1.26-9                     OK libsigsegv2                         2.10-2                       OK libSM6                              1.2.2-1                      OK libsmartcols1                       2.25.2-2                     OK libsqlite3_0                        3.14.1-1                     OK libssh2_1                           1.7.0-1                      OK libssp0                             5.4.0-1                      OK libstdc++6                          5.4.0-1                      OK libsynctex1                         20160520-3                   OK libtasn1_6                          4.9-1                        OK libtexlua52_5                       20160520-3                   OK libtexluajit2                       20160520-3                   OK libthai0                            0.1.21-1                     OK libtiff6                            4.0.6-1                      OK libtxc_dxtn                         1.0-1.20151227gitf6ec862     OK libunistring2                       0.9.6-1                      OK libusb0                             1.2.6.0-2                    OK libuuid-devel                       2.25.2-2                     OK libuuid1                            2.25.2-2                     OK libwebp5                            0.4.4-1                      OK libwebpmux1                         0.4.4-1                      OK libX11-xcb1                         1.6.3-1                      OK libX11_6                            1.6.3-1                      OK libXau6                             1.0.8-1                      OK libXaw7                             1.0.13-1                     OK libxcb-glx0                         1.12-1                       OK libxcb-render0                      1.12-1                       OK libxcb-shm0                         1.12-1                       OK libxcb1                             1.12-1                       OK libXdmcp6                           1.1.2-1                      OK libXext6                            1.3.3-1                      OK libXft2                             2.3.2-1                      OK libXi6                              1.7.6-1                      OK libxml2                             2.9.4-1                      OK libXmu6                             1.1.2-1                      OK libXpm4                             3.5.11-1                     OK libXrender1                         0.9.9-1                      OK libxslt                             1.1.29-1                     OK libXss1                             1.2.2-1                      OK libXt6                              1.1.5-1                      OK libyaml0_2                          0.1.6-2                      OK libzip2                             0.11.2-2                     OK libzzip0.13                         0.13.62-1                    OK login                               1.11-1                       OK m4                                  1.4.17-2                     OK man-db                              2.7.5-1                      OK mintty                              2.6.1-0                      OK ncurses                             6.0-8.20160917               OK netpbm                              10.74.05-1                   OK openssh                             7.3p1-2                      OK openssl                             1.0.2j-1                     OK p11-kit                             0.22.1-1                     OK p11-kit-trust                       0.22.1-1                     OK patch                               2.7.4-1                      OK patcher                             0.0.20040521-1               OK patchutils                          0.3.4-1                      OK perl                                5.22.2-1                     OK perl-autovivification               0.16-1                       OK perl-Business-ISBN                  3.002-1                      OK perl-Business-ISBN-Data             20140910.003-1               OK perl-Business-ISMN                  1.13-2                       OK perl-Business-ISSN                  0.91-2                       OK perl-Carp                           1.38-1                       OK perl-Class-Accessor                 0.34-1                       OK perl-Data-Compare                   1.25-2                       OK perl-Data-Dump                      1.23-1                       OK perl-Data-Uniqid                    0.12-1                       OK perl-Date-Simple                    3.03-2                       OK perl-Digest-SHA                     5.96-2                       OK perl-Encode-Locale                  1.05-1                       OK perl-Error                          0.17024-1                    OK perl-File-Find-Rule                 0.34-1                       OK perl-File-HomeDir                   1.00-3                       OK perl-File-Listing                   6.04-5                       OK perl-File-Slurp                     9999.19-5                    OK perl-File-Slurp-Tiny                0.004-1                      OK perl-File-Which                     1.21-1                       OK perl-HTML-Parser                    3.72-1                       OK perl-HTML-Tagset                    3.20-5                       OK perl-HTTP-Cookies                   6.01-5                       OK perl-HTTP-Daemon                    6.01-5                       OK perl-HTTP-Date                      6.02-5                       OK perl-HTTP-Message                   6.11-1                       OK perl-HTTP-Negotiate                 6.01-5                       OK perl-IO-HTML                        1.001-2                      OK perl-IO-Socket-SSL                  2.038-1                      OK perl-IO-String                      1.08-5                       OK perl-IPC-Cmd                        0.96-1                       OK perl-IPC-Run3                       0.048-2                      OK perl-libwww-perl                    6.15-1                       OK perl-Lingua-Translit                0.26-1                       OK perl-List-AllUtils                  0.11-1                       OK perl-List-SomeUtils                 0.53-1                       OK perl-List-UtilsBy                   0.10-1                       OK perl-Log-Log4perl                   1.47-1                       OK perl-LWP-MediaTypes                 6.02-5                       OK perl-LWP-Protocol-https             6.06-2                       OK perl-MIME-Charset                   1.012-2                      OK perl-Module-Implementation          0.09-1                       OK perl-Module-Load-Conditional        0.68-1                       OK perl-Module-Runtime                 0.014-1                      OK perl-Mojolicious                    7.05-1                       OK perl-Mozilla-CA                     20160104-1                   OK perl-Net-HTTP                       6.09-1                       OK perl-Net-SSLeay                     1.78-2                       OK perl-Number-Compare                 0.03-5                       OK perl-Pod-Simple                     3.32-1                       OK perl-Regexp-Common                  2016060801-2                 OK perl-Scalar-List-Utils              1.45-1                       OK perl-Socket                         2.024-2                      OK perl-TermReadKey                    2.33-1                       OK perl-Text-BibTeX                    0.76-1                       OK perl-Text-Glob                      0.10-1                       OK perl-Text-Roman                     3.5-1                        OK perl-TimeDate                       2.30-2                       OK perl-Tk                             804.033-1                    OK perl-Tk-Pod                         0.9942-1                     OK perl-Try-Tiny                       0.27-1                       OK perl-Unicode-Collate                1.14-1                       OK perl-Unicode-LineBreak              2016.003-1                   OK perl-Unicode-Normalize              1.25-1                       OK perl-URI                            1.71-1                       OK perl-WWW-RobotRules                 6.02-5                       OK perl-XML-LibXML                     2.0128-1                     OK perl-XML-LibXML-Simple              0.97-1                       OK perl-XML-LibXSLT                    1.95-2                       OK perl-XML-NamespaceSupport           1.11-5                       OK perl-XML-Parser                     2.44-2                       OK perl-XML-SAX                        0.99-5                       OK perl-XML-SAX-Base                   1.08-5                       OK perl-XML-Writer                     0.625-1                      OK perl_autorebase                     5.22.2-1                     OK perl_base                           5.22.2-1                     OK poppler-data                        0.4.7-1                      OK preview-latex                       11.89-1                      OK python                              2.7.10-1                     OK python-beautifulsoup                3.2.1-1                      OK python-cffi                         0.9.2-1                      OK python-chardet                      2.2.1-1                      OK python-docutils                     0.12-1                       OK python-imaging                      2.8.2-2                      OK python-jinja2                       2.7.3-1                      OK python-lxml                         3.4.4-1                      OK python-markupsafe                   0.23-1                       OK python-numpy                        1.9.2-1                      OK python-ply                          3.6-1                        OK python-pycparser                    2.12-1                       OK python-pygments                     2.0.2-1                      OK python-setuptools                   15.2-1                       OK python-simplejson                   3.6.5-1                      OK python-sphinx                       1.2.3-1                      OK rebase                              4.4.2-1                      OK rsync                               3.1.2-1                      OK ruby                                2.2.5-1                      OK ruby-json                           1.8.2-1                      OK ruby-minitest4                      4.7.5-1                      OK ruby-rake                           10.4.2-1                     OK ruby-rdoc                           4.2.0-1                      OK rubygems                            2.4.8-1                      OK run                                 1.3.4-2                      OK sed                                 4.2.2-3                      OK sgml-common                         0.6.3-3                      OK shared-mime-info                    1.6-3                        OK tar                                 1.28-1                       OK tcl                                 8.5.18-1                     OK tcl-tk                              8.5.18-1                     OK terminfo                            6.0-8.20160917               OK texlive                             20160520-3                   OK texlive-collection-basic            20160520-1                   OK texlive-collection-bibtexextra      20160520-1                   OK texlive-collection-binextra         20160520-1                   OK texlive-collection-fontsrecommended 20160520-1                   OK texlive-collection-latex            20160520-1                   OK texlive-collection-latexextra       20160520-1                   OK texlive-collection-latexrecommended 20160520-1                   OK texlive-collection-mathextra        20160520-1                   OK texlive-collection-pictures         20160520-1                   OK transfig                            3.2.5e-2                     OK tzdata                              2016f-1                      OK unzip                               6.0-15                       OK util-linux                          2.25.2-2                     OK vim-minimal                         7.4.2367-1                   OK w3m                                 0.5.3-3                      OK wget                                1.18-1                       OK which                               2.20-2                       OK xmlto                               0.0.26-1                     OK xz                                  5.2.2-1                      OK zlib0                               1.2.8-3                      OK</code></p></div><div id="comment-55921-info" class="comment-info"><span class="comment-age">(27 Sep '16, 09:13)</span> Mike_P</div></div><span id="55922"></span><div id="comment-55922" class="comment not_top_scorer"><div id="post-55922-score" class="comment-score"></div><div class="comment-text"><p>That looks OK, do you have a2x and a2x.py in <code>C:\Cygwin64\bin</code>?</p></div><div id="comment-55922-info" class="comment-info"><span class="comment-age">(27 Sep '16, 09:51)</span> grahamb ♦</div></div><span id="55923"></span><div id="comment-55923" class="comment not_top_scorer"><div id="post-55923-score" class="comment-score"></div><div class="comment-text"><p>both a2x files are present</p></div><div id="comment-55923-info" class="comment-info"><span class="comment-age">(27 Sep '16, 09:53)</span> Mike_P</div></div><span id="55924"></span><div id="comment-55924" class="comment not_top_scorer"><div id="post-55924-score" class="comment-score"></div><div class="comment-text"><p>And we can rule out the source tarball being the problem. I deleted all traces of it and the directories. Installed Git via chocalety. Cloned source. Prepped source and then msbuild. Same 4 errors.</p><p>I'm using python35. In all my previous Wireshark builds the last few years, I used Python27. Should I try Python27 since a2x is python associated?</p></div><div id="comment-55924-info" class="comment-info"><span class="comment-age">(27 Sep '16, 09:55)</span> Mike_P</div></div><span id="55927"></span><div id="comment-55927" class="comment not_top_scorer"><div id="post-55927-score" class="comment-score"></div><div class="comment-text"><p>I've recently moved over to Python 35 with no issues, apart from that a2x uses the Cygwin python, not the Windows version and this leads to all the faffing about with the tools\runa2x.sh wrapper on Windows to hide the native python.</p><p>You do have a difference in your build environment to mine, in that you have Cygwin on the path. I <em>never</em> do this.</p><p>I think we need to dig into the build output to see what's actually being called. Make sure there are no .xml files in your build docbook directory, re-run the build omitting the <code>/m</code> flag, redirecting the output to a file and search in there for <code>Generating developer-guide.xml</code> and post the context around there.</p></div><div id="comment-55927-info" class="comment-info"><span class="comment-age">(27 Sep '16, 10:10)</span> grahamb ♦</div></div><span id="55929"></span><div id="comment-55929" class="comment not_top_scorer"><div id="post-55929-score" class="comment-score"></div><div class="comment-text"><p>I removed cygwin from my path just to rule it out.</p><p>Deleted *.xml from \docbook directory.</p><p>Ran msbuild without /m and redirected output to log file. Logfile shows that unsuccessfulbuild because AlwaysCreate was specified:</p><pre><code>  Generating developer-guide.xml
  running a2x with args --verbose --attribute=build_dir=/cygdrive/c/Development/buildx64/docbook --attribute=docinfo --destination-dir=/cygdrive/c/Development/buildx64/docbook --asciidoc-opts= --no-xmllint --format=docbook --fop --stylesheet=ws.css /cygdrive/c/Development/wireshark/docbook/developer-guide.asciidoc
  a2x: args: [&#39;--verbose&#39;, &#39;--attribute=build_dir=/cygdrive/c/Development/buildx64/docbook&#39;, &#39;--attribute=docinfo&#39;, &#39;--destination-dir=/cygdrive/c/Development/buildx64/docbook&#39;, &#39;--asciidoc-opts=&#39;, &#39;--no-xmllint&#39;, &#39;--format=docbook&#39;, &#39;--fop&#39;, &#39;--stylesheet=ws.css&#39;, &#39;/cygdrive/c/Development/wireshark/docbook/developer-guide.asciidoc&#39;]
  a2x: resource files: []
  a2x: resource directories: [&#39;/etc/asciidoc/images&#39;, &#39;/etc/asciidoc/stylesheets&#39;]
  a2x: executing: &quot;/usr/bin/asciidoc.py&quot; --backend docbook -a &quot;a2x-format=docbook&quot;  --attribute &quot;build_dir=/cygdrive/c/Development/buildx64/docbook&quot; --attribute &quot;docinfo&quot; --verbose  --out-file &quot;/cygdrive/c/Development/buildx64/docbook/developer-guide.xml&quot; &quot;/cygdrive/c/Development/wireshark/docbook/developer-guide.asciidoc&quot;

  asciidoc: reading: /etc/asciidoc/asciidoc.conf
  asciidoc: reading: /cygdrive/c/Development/wireshark/docbook/asciidoc.conf
  asciidoc: reading: /cygdrive/c/Development/wireshark/docbook/developer-guide.asciidoc
  asciidoc: reading: /etc/asciidoc/docbook45.conf
  asciidoc: reading: /etc/asciidoc/filters/code/code-filter.conf
  asciidoc: reading: /etc/asciidoc/filters/graphviz/graphviz-filter.conf
  asciidoc: reading: /etc/asciidoc/filters/latex/latex-filter.conf
  asciidoc: reading: /etc/asciidoc/filters/music/music-filter.conf
  asciidoc: reading: /etc/asciidoc/filters/source/source-highlight-filter.conf
  asciidoc: reading: /etc/asciidoc/lang-en.conf
  asciidoc: reading: /cygdrive/c/Development/wireshark/docbook/asciidoc.conf
  asciidoc: writing: /cygdrive/c/Development/buildx64/docbook/developer-guide.xml
  asciidoc: developer-guide.asciidoc: line 3: evaluating: {include:/cygdrive/c/Development/wireshark/docbook/developer-guide-docinfo.xml}
  asciidoc: include: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_preface.asciidoc
  asciidoc: developer-guide.asciidoc: line 9: reading: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_preface.asciidoc
  asciidoc: include: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_chapter_env_intro.asciidoc
  asciidoc: developer-guide.asciidoc: line 20: reading: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_chapter_env_intro.asciidoc
  asciidoc: include: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_chapter_quick_setup.asciidoc
  asciidoc: developer-guide.asciidoc: line 22: reading: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_chapter_quick_setup.asciidoc
  asciidoc: include: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_chapter_sources.asciidoc
  asciidoc: developer-guide.asciidoc: line 24: reading: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_chapter_sources.asciidoc
  asciidoc: include: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_chapter_tools.asciidoc
  asciidoc: developer-guide.asciidoc: line 26: reading: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_chapter_tools.asciidoc
  asciidoc: include: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_chapter_libraries.asciidoc
  asciidoc: developer-guide.asciidoc: line 28: reading: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_chapter_libraries.asciidoc
  asciidoc: include: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_chapter_works.asciidoc
  asciidoc: developer-guide.asciidoc: line 39: reading: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_chapter_works.asciidoc
  asciidoc: include: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_chapter_build_intro.asciidoc
  asciidoc: developer-guide.asciidoc: line 41: reading: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_chapter_build_intro.asciidoc
  asciidoc: include: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_chapter_capture.asciidoc
  asciidoc: developer-guide.asciidoc: line 43: reading: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_chapter_capture.asciidoc
  asciidoc: include: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_chapter_dissection.asciidoc
  asciidoc: developer-guide.asciidoc: line 45: reading: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_chapter_dissection.asciidoc
  asciidoc: include: /cygdrive/c/Development/wireshark/docbook/wsluarm.asciidoc
  asciidoc: developer-guide.asciidoc: line 47: reading: /cygdrive/c/Development/wireshark/docbook/wsluarm.asciidoc
  asciidoc: include: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_dumper.asciidoc
  asciidoc: wsluarm.asciidoc: line 171: reading: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_dumper.asciidoc
  asciidoc: include: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_field.asciidoc
  asciidoc: wsluarm.asciidoc: line 172: reading: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_field.asciidoc
  asciidoc: include: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_gui.asciidoc
  asciidoc: wsluarm.asciidoc: line 173: reading: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_gui.asciidoc
  asciidoc: include: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_listener.asciidoc
  asciidoc: wsluarm.asciidoc: line 174: reading: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_listener.asciidoc
  asciidoc: include: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_pinfo.asciidoc
  asciidoc: wsluarm.asciidoc: line 175: reading: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_pinfo.asciidoc
  asciidoc: include: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_proto.asciidoc
  asciidoc: wsluarm.asciidoc: line 176: reading: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_proto.asciidoc
  asciidoc: include: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_tree.asciidoc
  asciidoc: wsluarm.asciidoc: line 177: reading: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_tree.asciidoc
  asciidoc: include: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_tvb.asciidoc
  asciidoc: wsluarm.asciidoc: line 178: reading: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_tvb.asciidoc
  asciidoc: include: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_file.asciidoc
  asciidoc: wsluarm.asciidoc: line 179: reading: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_file.asciidoc
  asciidoc: include: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_dir.asciidoc
  asciidoc: wsluarm.asciidoc: line 180: reading: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_dir.asciidoc
  asciidoc: include: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_util.asciidoc
  asciidoc: wsluarm.asciidoc: line 181: reading: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_util.asciidoc
  asciidoc: include: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_int64.asciidoc
  asciidoc: wsluarm.asciidoc: line 182: reading: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_int64.asciidoc
  asciidoc: include: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_struct.asciidoc
  asciidoc: wsluarm.asciidoc: line 183: reading: /cygdrive/c/Development/buildx64/docbook/wsluarm_src/wslua_struct.asciidoc
  asciidoc: include: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_chapter_userinterface.asciidoc
  asciidoc: developer-guide.asciidoc: line 49: reading: /cygdrive/c/Development/wireshark/docbook/wsdg_src/WSDG_chapter_userinterface.asciidoc
  asciidoc: include: /cygdrive/c/Development/wireshark/docbook/GPL_appendix.asciidoc
  asciidoc: developer-guide.asciidoc: line 51: reading: /cygdrive/c/Development/wireshark/docbook/GPL_appendix.asciidoc

FinalizeBuildStatus:
  Deleting file &quot;x64\RelWithDebInfo\generate_developer-guide.xml\generate.31F401FB.tlog\unsuccessfulbuild&quot;.
  Touching &quot;x64\RelWithDebInfo\generate_developer-guide.xml\generate.31F401FB.tlog\generate_developer-guide.xml.lastbuildstate&quot;.
Done Building Project &quot;C:\Development\buildx64\docbook\generate_developer-guide.xml.vcxproj&quot; (default targets).
Done Building Project &quot;C:\Development\buildx64\docbook\generate_developer-guide.xml.vcxproj.metaproj&quot; (default targets).
Project &quot;C:\Development\buildx64\docbook\developer_guide_docbook.vcxproj.metaproj&quot; (7) is building &quot;C:\Development\buildx64\docbook\developer_guide_docbook.vcxproj&quot; (10) on node 1 (default targets).
InitializeBuildStatus:
  Creating &quot;x64\RelWithDebInfo\developer_guide_docbook\develope.6C81E821.tlog\unsuccessfulbuild&quot; because &quot;AlwaysCreate&quot; was specified.
FinalizeBuildStatus:
  Deleting file &quot;x64\RelWithDebInfo\developer_guide_docbook\develope.6C81E821.tlog\unsuccessfulbuild&quot;.
  Touching &quot;x64\RelWithDebInfo\developer_guide_docbook\develope.6C81E821.tlog\developer_guide_docbook.lastbuildstate&quot;.
Done Building Project &quot;C:\Development\buildx64\docbook\developer_guide_docbook.vcxproj&quot; (default targets).
Done Building Project &quot;C:\Development\buildx64\docbook\developer_guide_docbook.vcxproj.metaproj&quot; (default targets).
Project &quot;C:\Development\buildx64\docbook\developer_guide_chm.vcxproj.metaproj&quot; (6) is building &quot;C:\Development\buildx64\docbook\developer_guide_chm.vcxproj&quot; (11) on node 1 (default targets).
InitializeBuildStatus:
  Creating &quot;x64\RelWithDebInfo\developer_guide_chm\develope.6F1AF36F.tlog\unsuccessfulbuild&quot; because &quot;AlwaysCreate&quot; was specified.
FinalizeBuildStatus:
  Deleting file &quot;x64\RelWithDebInfo\developer_guide_chm\develope.6F1AF36F.tlog\unsuccessfulbuild&quot;.
  Touching &quot;x64\RelWithDebInfo\developer_guide_chm\develope.6F1AF36F.tlog\developer_guide_chm.lastbuildstate&quot;.
Done Building Project &quot;C:\Development\buildx64\docbook\developer_guide_chm.vcxproj&quot; (default targets).
Done Building Project &quot;C:\Development\buildx64\docbook\developer_guide_chm.vcxproj.metaproj&quot; (default targets).
Project &quot;C:\Development\buildx64\docbook\developer_guides.vcxproj.metaproj&quot; (5) is building &quot;C:\Development\buildx64\docbook\developer_guides.vcxproj&quot; (12) on node 1 (default targets).
InitializeBuildStatus:
  Creating &quot;x64\RelWithDebInfo\developer_guides\developer_guides.tlog\unsuccessfulbuild&quot; because &quot;AlwaysCreate&quot; was specified.
FinalizeBuildStatus:
  Deleting file &quot;x64\RelWithDebInfo\developer_guides\developer_guides.tlog\unsuccessfulbuild&quot;.
  Touching &quot;x64\RelWithDebInfo\developer_guides\developer_guides.tlog\developer_guides.lastbuildstate&quot;.
Done Building Project &quot;C:\Development\buildx64\docbook\developer_guides.vcxproj&quot; (default targets).
Done Building Project &quot;C:\Development\buildx64\docbook\developer_guides.vcxproj.metaproj&quot; (default targets).
Project &quot;C:\Development\buildx64\docbook\all_guides.vcxproj.metaproj&quot; (4) is building &quot;C:\Development\buildx64\docbook\user_guides.vcxproj.metaproj&quot; (13) on node 1 (default targets).
Project &quot;C:\Development\buildx64\docbook\user_guides.vcxproj.metaproj&quot; (13) is building &quot;C:\Development\buildx64\docbook\user_guide_chm.vcxproj.metaproj&quot; (14) on node 1 (default targets).
Project &quot;C:\Development\buildx64\docbook\user_guide_chm.vcxproj.metaproj&quot; (14) is building &quot;C:\Development\buildx64\docbook\generate_user-guide.xml.vcxproj.metaproj&quot; (15) on node 1 (default targets).
Project &quot;C:\Development\buildx64\docbook\generate_user-guide.xml.vcxproj.metaproj&quot; (15) is building &quot;C:\Development\buildx64\docbook\generate_user-guide.xml.vcxproj&quot; (16) on node 1 (default targets).
InitializeBuildStatus:
  Creating &quot;x64\RelWithDebInfo\generate_user-guide.xml\generate.319C771F.tlog\unsuccessfulbuild&quot; because &quot;AlwaysCreate&quot; was specified.</code></pre></div><div id="comment-55929-info" class="comment-info"><span class="comment-age">(27 Sep '16, 10:46)</span> Mike_P</div></div><span id="55935"></span><div id="comment-55935" class="comment not_top_scorer"><div id="post-55935-score" class="comment-score"></div><div class="comment-text"><p>That looks quite normal and I can't see any errors. Do you still get errors in the build?</p><p>Re-reading the original question, it seemed to be failing due to missing files in the source directory, <code>docbook\user-guide-docinfo.xml</code> and <code>docbook\developer-guide-docinfo.xml</code>, and now I don't see those errors.<br />
</p><p>Has the switch to a git clone fixed that issue?</p><p>Did you delete and recreate your build dir and then re-run CMake when you switched to a git clone?</p></div><div id="comment-55935-info" class="comment-info"><span class="comment-age">(27 Sep '16, 15:09)</span> grahamb ♦</div></div><span id="55939"></span><div id="comment-55939" class="comment not_top_scorer"><div id="post-55939-score" class="comment-score"></div><div class="comment-text"><p>Did a clean then deleted everything in my buildx64 directory. Then did a cmake prep of files. Then msbuild from the buildx64 directory.</p><p>Guide error went away but I'm still failing with 4 of the same errors in my original post (ui, dfilter, wiretap, and text2pcap). Again, I have made no modifications to any source files. I got these 4 errors when I used the source tarball and now when I am using Git source clone.</p><pre><code>Build FAILED.

       &quot;C:\Development\buildx64\Wireshark.sln&quot; (default target) (1) -&gt;
       &quot;C:\Development\buildx64\ui\ui.vcxproj.metaproj&quot; (default target) (63) -&gt;
       &quot;C:\Development\buildx64\ui\ui.vcxproj&quot; (default target) (91) -&gt;
       (CustomBuild target) -&gt;
         C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. [C:\Development\buildx64\ui\ui.vcxproj]

       &quot;C:\Development\buildx64\Wireshark.sln&quot; (default target) (1) -&gt;
       &quot;C:\Development\buildx64\epan\dfilter\dfilter.vcxproj.metaproj&quot; (default target) (19) -&gt;
       &quot;C:\Development\buildx64\epan\dfilter\dfilter.vcxproj&quot; (default target) (110) -&gt;
         C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. [C:\Development\buildx64\epan\dfilter\dfilter.vcxproj]

       &quot;C:\Development\buildx64\Wireshark.sln&quot; (default target) (1) -&gt;
       &quot;C:\Development\buildx64\wiretap\wiretap.vcxproj.metaproj&quot; (default target) (74) -&gt;
       &quot;C:\Development\buildx64\wiretap\wiretap.vcxproj&quot; (default target) (125) -&gt;
         C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. [C:\Development\buildx64\wiretap\wiretap.vcxproj]

       &quot;C:\Development\buildx64\Wireshark.sln&quot; (default target) (1) -&gt;
       &quot;C:\Development\buildx64\text2pcap.vcxproj.metaproj&quot; (default target) (57) -&gt;
       &quot;C:\Development\buildx64\text2pcap.vcxproj&quot; (default target) (118) -&gt;
         C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. [C:\Development\buildx64\text2pcap.vcxproj]

    0 Warning(s)
    4 Error(s)

Time Elapsed 00:06:54.85</code></pre></div><div id="comment-55939-info" class="comment-info"><span class="comment-age">(28 Sep '16, 04:48)</span> Mike_P</div></div><span id="55941"></span><div id="comment-55941" class="comment not_top_scorer"><div id="post-55941-score" class="comment-score"></div><div class="comment-text"><p>Very confusing, there's no info there on what actually went wrong.</p><p>Please run the build again, omitting the /m flag and redirecting the output to a file and post that back here.</p></div><div id="comment-55941-info" class="comment-info"><span class="comment-age">(28 Sep '16, 06:00)</span> grahamb ♦</div></div><span id="55942"></span><div id="comment-55942" class="comment not_top_scorer"><div id="post-55942-score" class="comment-score"></div><div class="comment-text"><p>Did a clean, prep, and msbuild w/o m switch:</p><pre><code>Build FAILED.

&quot;C:\Development\buildx64\Wireshark.sln&quot; (default target) (1) -&gt;
&quot;C:\Development\buildx64\ALL_BUILD.vcxproj.metaproj&quot; (default target) (2) -&gt;
&quot;C:\Development\buildx64\androiddump.vcxproj.metaproj&quot; (default target) (22) -&gt;
&quot;C:\Development\buildx64\wiretap\wiretap.vcxproj.metaproj&quot; (default target) (23) -&gt;
&quot;C:\Development\buildx64\wiretap\wiretap.vcxproj&quot; (default target) (30) -&gt;
(CustomBuild target) -&gt; 
  C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. [C:\Development\buildx64\wiretap\wiretap.vcxproj]

&quot;C:\Development\buildx64\Wireshark.sln&quot; (default target) (1) -&gt;
&quot;C:\Development\buildx64\ALL_BUILD.vcxproj.metaproj&quot; (default target) (2) -&gt;
&quot;C:\Development\buildx64\copy_qt_dlls.vcxproj.metaproj&quot; (default target) (47) -&gt;
&quot;C:\Development\buildx64\wireshark.vcxproj.metaproj&quot; (default target) (48) -&gt;
&quot;C:\Development\buildx64\epan\epan.vcxproj.metaproj&quot; (default target) (49) -&gt;
&quot;C:\Development\buildx64\epan\dfilter\dfilter.vcxproj.metaproj&quot; (default target) (54) -&gt;
&quot;C:\Development\buildx64\epan\dfilter\dfilter.vcxproj&quot; (default target) (57) -&gt;
  C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. [C:\Development\buildx64\epan\dfilter\dfilter.vcxproj]

&quot;C:\Development\buildx64\Wireshark.sln&quot; (default target) (1) -&gt;
&quot;C:\Development\buildx64\ALL_BUILD.vcxproj.metaproj&quot; (default target) (2) -&gt;
&quot;C:\Development\buildx64\copy_qt_dlls.vcxproj.metaproj&quot; (default target) (47) -&gt;
&quot;C:\Development\buildx64\wireshark.vcxproj.metaproj&quot; (default target) (48) -&gt;
&quot;C:\Development\buildx64\ui\ui.vcxproj.metaproj&quot; (default target) (74) -&gt;
&quot;C:\Development\buildx64\ui\ui.vcxproj&quot; (default target) (75) -&gt;
  C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. [C:\Development\buildx64\ui\ui.vcxproj]

&quot;C:\Development\buildx64\Wireshark.sln&quot; (default target) (1) -&gt;
&quot;C:\Development\buildx64\ALL_BUILD.vcxproj.metaproj&quot; (default target) (2) -&gt;
&quot;C:\Development\buildx64\text2pcap.vcxproj.metaproj&quot; (default target) (104) -&gt;
&quot;C:\Development\buildx64\text2pcap.vcxproj&quot; (default target) (105) -&gt;
  C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. [C:\Development\buildx64\text2pcap.vcxproj]

    0 Warning(s)
    4 Error(s)

Time Elapsed 00:10:03.11</code></pre></div><div id="comment-55942-info" class="comment-info"><span class="comment-age">(28 Sep '16, 06:48)</span> Mike_P</div></div><span id="55944"></span><div id="comment-55944" class="comment not_top_scorer"><div id="post-55944-score" class="comment-score"></div><div class="comment-text"><p>Still not seeing anything indicating what the error is apart from an unspecified exit of cmd.exe.</p><p>Can you try this command line that will rebuild the dfilter project (chosen as it is the smallest), redirecting the output and posting it here again?</p><pre><code>msbuild /p:Configuration=RelWithDebInfo epan\dfilter\dfilter.vcxproj /t:Rebuild &gt; somefile.txt</code></pre></div><div id="comment-55944-info" class="comment-info"><span class="comment-age">(28 Sep '16, 07:21)</span> grahamb ♦</div></div><span id="55946"></span><div id="comment-55946" class="comment not_top_scorer"><div id="post-55946-score" class="comment-score"></div><div class="comment-text"><p>Here is the result of the dfilter build you requested:</p><pre><code>Microsoft (R) Build Engine version 12.0.31101.0
[Microsoft .NET Framework, version 4.0.30319.42000]
Copyright (C) Microsoft Corporation. All rights reserved.

Build started 9/28/2016 10:37:57 AM.
Project &quot;C:\Development\buildx64\epan\dfilter\dfilter.vcxproj&quot; on node 1 (Rebuild target(s)).
_PrepareForClean:
  Deleting file &quot;dfilter.dir\RelWithDebInfo\dfilter.tlog\dfilter.lastbuildstate&quot;.
Project &quot;C:\Development\buildx64\epan\dfilter\dfilter.vcxproj&quot; (1) is building &quot;C:\Development\buildx64\ZERO_CHECK.vcxproj&quot; (2) on node 1 (Clean target(s)).
_PrepareForClean:
  Deleting file &quot;x64\RelWithDebInfo\ZERO_CHECK\ZERO_CHECK.tlog\ZERO_CHECK.lastbuildstate&quot;.
Done Building Project &quot;C:\Development\buildx64\ZERO_CHECK.vcxproj&quot; (Clean target(s)).
Project &quot;C:\Development\buildx64\epan\dfilter\dfilter.vcxproj&quot; (1) is building &quot;C:\Development\buildx64\tools\lemon\lemon.vcxproj&quot; (3) on node 1 (Clean target(s)).
_PrepareForClean:
  Deleting file &quot;lemon.dir\RelWithDebInfo\lemon.tlog\lemon.lastbuildstate&quot;.
Done Building Project &quot;C:\Development\buildx64\tools\lemon\lemon.vcxproj&quot; (Clean target(s)).
Project &quot;C:\Development\buildx64\epan\dfilter\dfilter.vcxproj&quot; (1) is building &quot;C:\Development\buildx64\ZERO_CHECK.vcxproj&quot; (2:3) on node 1 (default targets).
InitializeBuildStatus:
  Creating &quot;x64\RelWithDebInfo\ZERO_CHECK\ZERO_CHECK.tlog\unsuccessfulbuild&quot; because &quot;AlwaysCreate&quot; was specified.
CustomBuild:
  Checking Build System
  CMake does not need to re-run because C:/Development/buildx64/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/zlib/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/capchild/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/caputils/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/codecs/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/doc/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/docbook/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/crypt/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dfilter/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/HI2Operations/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/acp133/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/acse/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/ansi_map/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/ansi_tcap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/atn-cm/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/atn-cpdlc/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/atn-ulcs/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/c1222/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/camel/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/cdt/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/charging_ase/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/cmip/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/cmp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/cms/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/credssp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/crmf/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/dap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/disp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/dop/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/dsp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/ess/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/ftam/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/goose/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/gprscdr/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/gsm_map/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/h225/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/h235/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/h245/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/h248/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/h282/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/h283/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/h323/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/h450/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/h450-ros/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/h460/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/h501/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/hnbap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/idmp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/ilp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/inap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/isdn-sup/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/kerberos/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/lcsap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/ldap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/logotypecertextn/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/lpp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/lppa/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/lppe/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/lte-rrc/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/m2ap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/m3ap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/mms/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/mpeg-audio/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/mpeg-pes/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/nbap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/ns_cert_exts/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/novell_pkis/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/ocsp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/p1/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/p22/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/p7/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/p772/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/pcap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/pkcs1/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/pkcs12/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/pkinit/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/pkix1explicit/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/pkix1implicit/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/pkixac/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/pkixproxy/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/pkixqualified/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/pkixtsp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/pres/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/q932/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/q932-ros/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/qsig/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/ranap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/rnsap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/ros/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/rrc/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/rrlp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/rtse/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/rua/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/s1ap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/sabp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/sbc-ap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/smrse/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/snmp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/spnego/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/sv/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/t124/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/t125/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/t38/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/tcap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/tetra/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/ulp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/wlancertextn/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/x2ap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/x509af/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/x509ce/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/x509if/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/asn1/x509sat/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/dcerpc/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/dissectors/pidl/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/ftypes/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/nghttp2/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/wmem/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/epan/wslua/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/randpkt_core/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/tools/lemon/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/ui/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/wiretap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/writecap/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/wsutil/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/ui/gtk/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/ui/qt/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/plugins/docsis/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/plugins/ethercat/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/plugins/gryphon/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/plugins/irda/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/plugins/m2m/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/plugins/mate/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/plugins/opcua/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/plugins/profinet/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/plugins/stats_tree/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/plugins/unistim/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/plugins/wimax/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/plugins/wimaxasncp/CMakeFiles/generate.stamp is up-to-date.
  CMake does not need to re-run because C:/Development/buildx64/plugins/wimaxmacphy/CMakeFiles/generate.stamp is up-to-date.
FinalizeBuildStatus:
  Deleting file &quot;x64\RelWithDebInfo\ZERO_CHECK\ZERO_CHECK.tlog\unsuccessfulbuild&quot;.
  Touching &quot;x64\RelWithDebInfo\ZERO_CHECK\ZERO_CHECK.tlog\ZERO_CHECK.lastbuildstate&quot;.
Done Building Project &quot;C:\Development\buildx64\ZERO_CHECK.vcxproj&quot; (default targets).
Project &quot;C:\Development\buildx64\epan\dfilter\dfilter.vcxproj&quot; (1) is building &quot;C:\Development\buildx64\tools\lemon\lemon.vcxproj&quot; (3:2) on node 1 (default targets).
InitializeBuildStatus:
  Creating &quot;lemon.dir\RelWithDebInfo\lemon.tlog\unsuccessfulbuild&quot; because &quot;AlwaysCreate&quot; was specified.
CustomBuild:
  Building Custom Rule C:/Development/wireshark/tools/lemon/CMakeLists.txt
  CMake does not need to re-run because C:\Development\buildx64\tools\lemon\CMakeFiles\generate.stamp is up-to-date.
ClCompile:
  C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\amd64\CL.exe /c /IC:\Development\buildx64\zlib /I&quot;C:\development\wireshark\wireshark-win64-libs\zlib-1.2.8-ws&quot; /IC:\Development\buildx64 /IC:\Development\wireshark /IC:\Development\wireshark\epan /IC:\Development\wireshark\tools\lemon /I&quot;C:\Development\wireshark\wireshark-win64-libs\AirPcap_Devpack_4_1_0_1622\Airpcap_Devpack\include&quot; /I&quot;C:\Development\wireshark\wireshark-win64-libs\c-ares-1.11.0-win64ws\include&quot; /I&quot;C:\Development\wireshark\wireshark-win64-libs\gnutls-3.2.15-2.9-win64ws\include&quot; /I&quot;C:\Development\wireshark\wireshark-win64-libs\GeoIP-1.6.6-win64ws\include&quot; /I&quot;C:\Development\wireshark\wireshark-win64-libs\gtk2\include\glib-2.0&quot; /I&quot;C:\Development\wireshark\wireshark-win64-libs\gtk2\lib\glib-2.0\include&quot; /I&quot;C:\Development\wireshark\wireshark-win64-libs\gtk2\include\glib-2.0\glib&quot; /I&quot;C:\Development\wireshark\wireshark-win64-libs\gtk2\include\gtk-2.0&quot; /I&quot;C:\Development\wireshark\wireshark-win64-libs\gtk2\include&quot; /I&quot;C:\Development\wireshark\wireshark-win64-libs\gtk2\include\freetype2&quot; /I&quot;C:\Development\wireshark\wireshark-win64-libs\gtk2\include\atk-1.0&quot; /I&quot;C:\Development\wireshark\wireshark-win64-libs\gtk2\include\gdk-pixbuf-2.0&quot; /I&quot;C:\Development\wireshark\wireshark-win64-libs\gtk2\include\cairo&quot; /I&quot;C:\Development\wireshark\wireshark-win64-libs\gtk2\include\pango-1.0&quot; /I&quot;C:\Development\wireshark\wireshark-win64-libs\gtk2\lib\gtk-2.0\include&quot; /I&quot;C:\Development\wireshark\wireshark-win64-libs\kfw-3-2-2-x64-ws\include&quot; /I&quot;C:\Development\wireshark\wireshark-win64-libs\libssh-0.7.2-win64ws\include&quot; /I&quot;C:\Development\wireshark\wireshark-win64-libs\lua5.2.4\include&quot; /I&quot;C:\Development\wireshark\wireshark-win64-libs\WpdPack\Include&quot; /I&quot;C:\Development\wireshark\wireshark-win64-libs\portaudio_v19_2\include&quot; /I&quot;C:\development\wireshark\wireshark-win64-libs\portaudio_v19_2\src\common&quot; /I&quot;C:\development\wireshark\wireshark-win64-libs\portaudio_v19_2\src\os\win&quot; /IC:\Qt\Qt5.7.0\5.7\msvc2013_64\include /IC:\Qt\Qt5.7.0\5.7\msvc2013_64\include\QtCore /I&quot;C:\Qt\Qt5.7.0\5.7\msvc2013_64\.\mkspecs\win32-msvc2013&quot; /IC:\Qt\Qt5.7.0\5.7\msvc2013_64\include\QtMultimedia /IC:\Qt\Qt5.7.0\5.7\msvc2013_64\include\QtNetwork /IC:\Qt\Qt5.7.0\5.7\msvc2013_64\include\QtGui /IC:\Qt\Qt5.7.0\5.7\msvc2013_64\include\QtPrintSupport /IC:\Qt\Qt5.7.0\5.7\msvc2013_64\include\QtWidgets /IC:\Qt\Qt5.7.0\5.7\msvc2013_64\include\QtSvg /IC:\Qt\Qt5.7.0\5.7\msvc2013_64\include\QtWinExtras /I&quot;C:\Development\wireshark\wireshark-win64-libs\libsmi-svn-40773-win64ws\include&quot; /I&quot;C:\Development\wireshark\wireshark-win64-libs\WinSparkle-0.3-44-g2c8d9d3-win64ws&quot; /Zi /nologo /W3 /WX /MP /O2 /Ob1 /D WIN32 /D _WINDOWS /D NDEBUG /D WIN32_LEAN_AND_MEAN /D MSC_VER_REQUIRED=1800 /D _CRT_SECURE_NO_DEPRECATE /D NOMINMAX /D PSAPI_VERSION=1 /D BUILD_WINDOWS /D _ALLOW_KEYWORD_MACROS /D WINPCAP_VERSION=4_1_3 /D &quot;CMAKE_INTDIR=\&quot;RelWithDebInfo\&quot;&quot; /D _MBCS /Gm- /MD /GS /fp:precise /Zc:wchar_t /Zc:forScope /Fo&quot;lemon.dir\RelWithDebInfo\\&quot; /Fd&quot;lemon.dir\RelWithDebInfo\vc120.pdb&quot; /Gd /TC /wd4200 /errorReport:queue  /Zo /w34295 /w34189 C:\Development\wireshark\tools\lemon\lemon.c
  lemon.c
Link:
  C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\amd64\link.exe /ERRORREPORT:QUEUE /OUT:&quot;C:\Development\buildx64\run\RelWithDebInfo\lemon.exe&quot; /INCREMENTAL /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib shell32.lib ole32.lib oleaut32.lib uuid.lib comdlg32.lib advapi32.lib /MANIFEST /MANIFESTUAC:&quot;level=&#39;asInvoker&#39; uiAccess=&#39;false&#39;&quot; /manifest:embed /DEBUG /PDB:&quot;C:/Development/buildx64/run/RelWithDebInfo/lemon.pdb&quot; /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:&quot;C:/Development/buildx64/run/RelWithDebInfo/lemon.lib&quot; /MACHINE:X64  /machine:x64 lemon.dir\RelWithDebInfo\lemon.obj
  lemon.vcxproj -&gt; C:\Development\buildx64\run\RelWithDebInfo\lemon.exe
FinalizeBuildStatus:
  Deleting file &quot;lemon.dir\RelWithDebInfo\lemon.tlog\unsuccessfulbuild&quot;.
  Touching &quot;lemon.dir\RelWithDebInfo\lemon.tlog\lemon.lastbuildstate&quot;.
Done Building Project &quot;C:\Development\buildx64\tools\lemon\lemon.vcxproj&quot; (default targets).
InitializeBuildStatus:
  Touching &quot;dfilter.dir\RelWithDebInfo\dfilter.tlog\unsuccessfulbuild&quot;.
CustomBuild:
  Building Custom Rule C:/Development/wireshark/epan/dfilter/CMakeLists.txt
  CMake does not need to re-run because C:\Development\buildx64\epan\dfilter\CMakeFiles\generate.stamp is up-to-date.
  Generating scanner.c, scanner_lex.h
  C:/cygwin64/bin/flex.exe -&gt; /usr/bin/flex.exe
  C:/Development/wireshark/tools/runlex.sh: line 86: C:/Program: No such file or directory
  flex: could not create --header-file=./_lex.h
  /usr/bin/flex.exe failed: exit status 1
C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. [C:\Development\buildx64\epan\dfilter\dfilter.vcxproj]
Done Building Project &quot;C:\Development\buildx64\epan\dfilter\dfilter.vcxproj&quot; (Rebuild target(s)) -- FAILED.

Build FAILED.

&quot;C:\Development\buildx64\epan\dfilter\dfilter.vcxproj&quot; (Rebuild target) (1) -&gt;
(CustomBuild target) -&gt; 
  C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: &quot;cmd.exe&quot; exited with code 1. [C:\Development\buildx64\epan\dfilter\dfilter.vcxproj]

    0 Warning(s)
    1 Error(s)

Time Elapsed 00:00:04.72</code></pre></div><div id="comment-55946-info" class="comment-info"><span class="comment-age">(28 Sep '16, 07:41)</span> Mike_P</div></div></div><div id="comment-tools-55899" class="comment-tools"><span class="comments-showing"> showing 5 of 23 </span> <a href="#" class="show-all-comments-link">show 18 more comments</a></div><div class="clear"></div><div id="comment-55899-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55947"></span>

<div id="answer-container-55947" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55947-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Now we're getting somewhere:</p><pre><code>Generating scanner.c, scanner_lex.h
C:/cygwin64/bin/flex.exe -&gt; /usr/bin/flex.exe
C:/Development/wireshark/tools/runlex.sh: line 86: C:/Program: No such file or directory
flex: could not create --header-file=./_lex.h
/usr/bin/flex.exe failed: exit status 1</code></pre><p>Looking at line 86 or tools\runlex.sh indicates that it relies on sed, expecting to be using the Cygwin version. I suspect that somewhere on your path there is a non-Cygwin version in <code>C:\Program Files\...</code>, possibly <code>C:\Program Files (x86)\GnuWin32\bin</code>.</p><p>Can you look in the CMakeCache.txt file in your build directory for <code>SED_EXECUTABLE:FILEPATH=</code> and post the whole line, that will hopefully show you where the offending sed lives?</p><p>To fix this remove the offending directory from the path, delete CMakeCache.txt and re-run the CMake and build steps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '16, 08:06</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></p></div></div><div id="comments-container-55947" class="comments-container"><span id="55948"></span><div id="comment-55948" class="comment"><div id="post-55948-score" class="comment-score"></div><div class="comment-text"><p>Bullseye!</p><pre><code>//Path to a program.
SED_EXECUTABLE:FILEPATH=C:/Program Files (x86)/GnuWin32/bin/sed.exe</code></pre></div><div id="comment-55948-info" class="comment-info"><span class="comment-age">(28 Sep '16, 08:11)</span> Mike_P</div></div><span id="55949"></span><div id="comment-55949" class="comment"><div id="post-55949-score" class="comment-score"></div><div class="comment-text"><p>Removed from path, cleaned folders, building now.........</p></div><div id="comment-55949-info" class="comment-info"><span class="comment-age">(28 Sep '16, 08:19)</span> Mike_P</div></div><span id="55955"></span><div id="comment-55955" class="comment"><div id="post-55955-score" class="comment-score"></div><div class="comment-text"><p>SUCCESS!</p><p>I need ccrypt, gzip, and tar provided by GnuWin32 and with it being in my path, it was using the wrong sed as you pointed out. By adding cygwin\bin to my path in front of GnuWin32, I can now compile Wireshark source with no errors.</p><p>I cannot thank you enough for all your help!!</p></div><div id="comment-55955-info" class="comment-info"><span class="comment-age">(28 Sep '16, 08:42)</span> Mike_P</div></div><span id="55958"></span><div id="comment-55958" class="comment"><div id="post-55958-score" class="comment-score"></div><div class="comment-text"><p>Note that I don't recommend adding Cygwin to your path for Wireshark dev, it has caused other issues in the past.</p><p>What I would recommend is creating a batch file, or PowerShell script if you use that for your shell, to add the Wireshark specific env vars and modify the path to suit and run that when starting a shell for Wireshark dev. Much easier done in Powershell than dos batch though.</p></div><div id="comment-55958-info" class="comment-info"><span class="comment-age">(28 Sep '16, 08:50)</span> grahamb ♦</div></div><span id="55959"></span><div id="comment-55959" class="comment"><div id="post-55959-score" class="comment-score"></div><div class="comment-text"><p>I've re-arranged the deckchairs so we now have an answer you can accept. Sorry it took so long to get there, a few red herrings were caught along the way.</p></div><div id="comment-55959-info" class="comment-info"><span class="comment-age">(28 Sep '16, 08:53)</span> grahamb ♦</div></div></div><div id="comment-tools-55947" class="comment-tools"></div><div class="clear"></div><div id="comment-55947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

